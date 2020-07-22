#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:40:29 2020

@author: amelielaurens

Source : A simple model for nanofiber formation by rotary jet-spinning
by mellado et al.

Goal : Prediction of the final radius for various polymer surface tension.

Select the machine and the polymer for which we want to run the code.

Inputs : Concerning the polymer : the density, the viscosity
         Concerning the machine : the reservoir radius, the collector radius,
                                  the orifice radius,
                                  the angular viscosity of the spinneret.

All data are in SI units.
"""

from models_RJS import *
import numpy
import matplotlib.pyplot as plt

discretisation = 20
# The higher the discretisation number is, the finer the discretisation will be,
# there will be more points on the graphic.

# Choose one machine and one polymer
# Machines :
# Super Floss Maxx
s0 = 0.06985
Rc = 0.3302
omega = 57.5
orifice_radius = 0.001512

# CANDY-V001
# s0 = 0.0635
# Rc = 0.254
# omega = 40.
# orifice_radius = 0.000267

# Polymers :
# PP
rho = 900.
mu = 0.63

# PLA
# rho = 1250.
# mu = 0.113

# If we want to make the user enter its own values
# s0 = float(input("Enter the radius of the reservoir in m : "))
# discretisation = int(input("Enter an int for the mesh's thinness : "))
# rho = float(input("Enter the density of the polymer in kg/m^3 : "))
# mu = float(input("Enter the viscosity of the polymer in Pa.s : "))
# Rc = float(input("Enter the radius of the collector in m : "))
# omega = float(input("Enter the angular velocity in rounds per second : "))
# orifice_radius = float(input("Enter the radius of the orifice in m : "))

surface_tension = numpy.linspace(0.02, 0.06, discretisation)

omega_th = []
initial_velocity = []
for l in range(discretisation):
    omega_th.append(critical_rotational_velocity_threshold(surface_tension[l], orifice_radius,
                                                           s0, rho))
    initial_velocity.append(Initial_velocity(omega_th[l], s0))
omega_th = numpy.array(omega_th)
initial_velocity = numpy.array(initial_velocity)

nu = kinematic_viscosity(mu, rho)

final_radius = []
for k in range(discretisation):
    final_radius.append(final_radius_approx(orifice_radius, initial_velocity[k],
                                            nu, Rc, omega))
final_radius = numpy.array(final_radius)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for i in range(discretisation):
    axes.plot(surface_tension[i], final_radius[i], 'ro')
axes.grid()
axes.set_xlabel("Surface tension (kg/s^2)", fontsize=16)
axes.set_ylabel("Final radius (m)", fontsize=16)
# Choose which title
# axes.set_title("Final radius as a function of the surface tension ", fontsize=16)
axes.set_title("Super Floss Maxx  / PP", fontsize=16, y=1.)
# axes.set_title("Super Floss Maxx  / PLA", fontsize=16, y=1.)
# axes.set_title("CANDY-V001  / PP", fontsize=16, y=1.)
# axes.set_title("CANDY-V001  / PLA", fontsize=16, y=1.)

# Plot a zoomed graphic on the small radius below 0.00002 m
fig2 = plt.figure()
axes = fig2.add_subplot(1, 1, 1)

for i in range(discretisation):
    if final_radius[i] <= 0.00002:
        axes.plot(surface_tension[i], final_radius[i], 'bo')
axes.grid()
axes.set_xlabel("Surface tension (kg/s^2)", fontsize=16)
axes.set_ylabel("Final radius  (m)", fontsize=16)

# Choose one title
# axes.set_title("ZOOM Final radius as a function of the surface tension ", fontsize=16)
axes.set_title("ZOOM Super Floss Maxx  / PP ", fontsize=16)
# axes.set_title("ZOOM Super Floss Maxx  / PLA", fontsize=16, y=1.)
# axes.set_title("ZOOM CANDY-V001  / PP", fontsize=16, y=1.)
# axes.set_title("ZOOM CANDY-V001  / PLA", fontsize=16, y=1.)
