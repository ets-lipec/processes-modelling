#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:27:46 2020

@author: amelielaurens
"""

# Predict an approximation of the final radius for various angular velocities

from models_RJS import *
import numpy
import matplotlib.pyplot as plt


discretisation = 20 #The higher the discretisation number is, the finer the discretisation will be, there will be more points on the graphic


#Choose one machine and one polymer
#Machines
#Super Floss Maxx
#s0 = 0.06985
#Rc = 0.3302
#orifice_radius = 0.001512

#CANDY-V001
s0 = 0.0635
Rc = 0.254
orifice_radius = 0.000267


#Polymers
#PP
#surface_tension = 0.0436
#rho = 900.
#mu = 0.63

#PLA
surface_tension = 0.0248
rho = 1250.
mu = 0.113


#If we want the user to enter its own values
#s0 = float(input("Enter the radius of the reservoir in m : "))
#surface_tension =float(input("Enter the surface tension in kg/s^2 : "))
#orifice_radius = float(input("Enter the radius of the orifice in m : "))
#rho = float(input("Enter the density of the polymer in kg/m^3 : "))
#mu = float(input("Enter the viscosity of the polymer in Pa.s : "))
#Rc = float(input("Enter the radius of the collector in m : "))
#discretisation = int(input("Enter an int for the mesh's thinness : "))

omega_th=critical_rotational_velocity_threshold(surface_tension, orifice_radius, s0, rho)
initial_velocity=Initial_velocity(omega_th, s0)

nu = kinematic_viscosity(mu, rho)

omega = numpy.linspace(4000//60, 37000//60, discretisation)

final_radius = []
for k in range(discretisation):
    final_radius.append(final_radius_approx(orifice_radius, initial_velocity, nu, Rc, omega[k]))
final_radius=numpy.array(final_radius)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for i in range(discretisation):
    axes.plot(omega[i], final_radius[i], 'ro')
axes.grid()
axes.set_xlabel("Angular velocity (rounds per second)", fontsize=16)
axes.set_ylabel("Final radius (m)", fontsize=16)

#Choose one title
#axes.set_title("Final radius as a function of the angular velocity ", fontsize=16)
#axes.set_title("Super Floss Maxx  / PP ", fontsize=16)
#axes.set_title("Super Floss Maxx  / PLA", fontsize=16, y=1.)
#axes.set_title("CANDY-V001  / PP", fontsize=16, y=1.)
axes.set_title("CANDY-V001  / PLA", fontsize=16, y=1.)

