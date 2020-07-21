#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:10:31 2020

@author: amelielaurens

Source : A simple model for nanofiber formation by rotary jet-spinning
by mellado et al.

Goal : Prediction of the radius of the jet in steady state as a function of
the axial coordinate x.

Select the machine and the polymer for which we want to run the code.

Inputs : Concerning the polymer : the surface tension, the density, the viscosity
         Concerning the machine : the reservoir radius, the collector radius,
         the orifice radius, the angular viscosity of the spinneret.

All data are in SI units.

"""

from models_RJS import *
import numpy
import matplotlib.pyplot as plt


discretisation = 20
# The higher the discretisation number is, the finer the discretisation will be,
# there will be more points on the graphic.


# Choose one machine and one polymer
# Machines
# Super Floss Maxx
# s0 = 0.06985
# Rc = 0.3302
# orifice_radius = 0.001512
# omega = 57.5

# CANDY-V001
s0 = 0.0635
Rc = 0.254
orifice_radius = 0.000267
omega = 40.


# Polymers
# PP
# surface_tension = 0.0436
# rho = 900.
# mu = 0.63

# PLA
surface_tension = 0.0248
rho = 1250.
mu = 0.113


# If we want the user to enter its own values
# surface_tension =float(input("Enter the surface tension in kg/s^2 : "))
# Rc = float(input("Enter the radius of the collector in m : "))
# s0 = float(input("Enter the radius of the reservoir in m : "))
# discretisation = int(input("Enter an int for the mesh's thinness : "))
# orifice_radius = float(input("Enter the radius of the orifice in m : "))
# rho = float(input("Enter the density of the polymer in kg/m^3 : "))
# mu = float(input("Enter the viscosity of the polymer in Pa.s : "))
# omega = float(input("Enter the angular velocity in rounds per second : "))


x_position = numpy.linspace(0, Rc-s0, discretisation)

omega_th = critical_rotational_velocity_threshold(surface_tension,
                                                  orifice_radius, s0, rho)
initial_velocity = Initial_velocity(omega_th, s0)
Sigma = []
for l in range(discretisation):
    Sigma.append(sigma(surface_tension, x_position[l], orifice_radius,
                       initial_velocity))
Sigma = numpy.array(Sigma)


radius = []
for k in range(1, discretisation):
    radius.append(Radius(orifice_radius, rho, initial_velocity, x_position[k],
                         mu, Sigma[k], omega))
radius = numpy.array(radius)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for i in range(discretisation-1):
    axes.plot(x_position[i], radius[i], 'ro')
axes.grid()
axes.set_xlabel("Axial coordinate x (m)", fontsize=16)
axes.set_ylabel("Radius (m)", fontsize=16)

# Choose one title
# axes.set_title("Radius of the jet as a function of the axial coordinate ", fontsize=16)
# axes.set_title("Super Floss Maxx  / PP ", fontsize=16)
# axes.set_title("Super Floss Maxx  / PLA", fontsize=16, y=1.)
# axes.set_title("CANDY-V001  / PP", fontsize=16, y=1.)
axes.set_title("CANDY-V001  / PLA", fontsize=16, y=1.)

# Plot a zoomed graphic on the small radius below 0.00002 m
fig2 = plt.figure()
axes = fig2.add_subplot(1, 1, 1)

for i in range(discretisation-1):
    if radius[i] <= 0.00002:
        axes.plot(x_position[i], radius[i], 'bo')
axes.grid()
axes.set_xlabel("Axial coordinate x (m)", fontsize=16)
axes.set_ylabel("Radius (m)", fontsize=16)

# Choose one title
# axes.set_title("ZOOM Radius of the jet as a function of the axial coordinate ", fontsize=16)
# axes.set_title("ZOOM Super Floss Maxx  / PP ", fontsize=16)
# axes.set_title("ZOOM Super Floss Maxx  / PLA", fontsize=16, y=1.)
# axes.set_title("ZOOM CANDY-V001  / PP", fontsize=16, y=1.)
axes.set_title("ZOOM CANDY-V001  / PLA", fontsize=16, y=1.)
