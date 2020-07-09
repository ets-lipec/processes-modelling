#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:10:31 2020

@author: amelielaurens
"""

from models_RJS import *
import numpy
import matplotlib.pyplot as plt

# predict the radius of the jet in steady state as a function of the axial coordinate x
surface_tension =float(input("Enter the surface tension in kg/s^2 : "))
Rc = float(input("Enter the radius of the collector in m : "))
s0 = float(input("Enter the radius of the reservoir in m : "))
discretisation = int(input("Enter an int for the mesh's thinness : "))
x_position = numpy.linspace(0, Rc-s0, discretisation)
r0 = float(input("Enter the radius of the orifice in m : "))
rho = float(input("Enter the density of the polymer in kg/m^3 : "))
omega_th=critical_rotational_velocity_threshold(surface_tension, r0, s0, rho)
initial_velocity=Initial_velocity(omega_th, s0)
Sigma = []
for l in range(discretisation):
    Sigma.append(sigma(surface_tension, x_position[l], r0, initial_velocity))
Sigma=numpy.array(Sigma)
mu = float(input("Enter the viscosity of the polymer in Pa.s : "))
omega = float(input("Enter the angular velocity in rounds per second : "))


radius=[]
for k in range(1,discretisation):
    radius.append(Radius(r0, rho, initial_velocity, x_position[k], mu, Sigma[k], omega))
radius = numpy.array(radius)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for i in range(discretisation-1):
    axes.plot(x_position[i], radius[i], 'ro')
axes.grid()
axes.set_xlabel("Axial coordinate x (m)", fontsize=16)
axes.set_ylabel("Radius (m)", fontsize=16)
axes.set_title("Radius of the jet as a function of the axial coordinate ", fontsize=16)
#axes.set_title("CANDY-V001 / PLA", fontsize=16)

# tracer un graphe zoomé sur les petits rayons inférieurs à 0.00010 m
fig2 = plt.figure()
axes = fig2.add_subplot(1, 1, 1)

for i in range(discretisation-1):
    if radius[i]<=0.00010:
         axes.plot(x_position[i], radius[i], 'bo')
axes.grid()
axes.set_xlabel("Axial coordinate x (m)", fontsize=16)
axes.set_ylabel("Radius (m)", fontsize=16)
axes.set_title("ZOOM Radius of the jet as a function of the axial coordinate ", fontsize=16)
#axes.set_title("ZOOM CANDY-V001 / PLA", fontsize=16)
