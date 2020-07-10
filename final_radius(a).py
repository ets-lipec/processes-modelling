#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:25:04 2020

@author: amelielaurens
"""


from models_RJS import *
import numpy
import matplotlib.pyplot as plt

# Predict an approximation of the final radius for various orifice radius
s0 = float(input("Enter the radius of the reservoir in m : "))
surface_tension =float(input("Enter the surface tension in kg/s^2 : "))
discretisation = int(input("Enter an int for the mesh's thinness : "))
orifice_radius = numpy.linspace(0.0001, 0.001, discretisation)
rho = float(input("Enter the density of the polymer in kg/m^3 : "))
omega_th=[]
initial_velocity=[]
for l in range(discretisation):
    omega_th.append(critical_rotational_velocity_threshold(surface_tension, orifice_radius[l], s0, rho))
    initial_velocity.append(Initial_velocity(omega_th[l], s0))
omega_th=numpy.array(omega_th)
initial_velocity=numpy.array(initial_velocity)
mu = float(input("Enter the viscosity of the polymer in Pa.s : "))
nu = kinematic_viscosity(mu, rho)
Rc = float(input("Enter the radius of the collector in m : "))
omega = float(input("Enter the angular velocity in rounds per second : "))


final_radius = []
for k in range(discretisation):
    final_radius.append(final_radius_approx(orifice_radius[k], initial_velocity[k], nu, Rc, omega))
final_radius=numpy.array(final_radius)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for i in range(discretisation):
    axes.plot(orifice_radius[i], final_radius[i], 'ro')
axes.grid()
axes.set_xlabel("Radius of the orifice (m)", fontsize=16)
axes.set_ylabel("Final radius (m)", fontsize=16)
axes.set_title("Final radius as a function of the orifice radius ", fontsize=16)