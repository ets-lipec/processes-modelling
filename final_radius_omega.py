#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:27:46 2020

@author: amelielaurens

Source : A simple model for nanofiber formation by rotary jet-spinning
by mellado et al.

Goal : Prediction of the final radius for various angular velocities.

Select the machine and the polymer for which we want to run the code and ajust values
in deck.yaml file.

Polymer parameters : the density, the viscosity, the surface tension
Machine parameters  : the reservoir radius, the collector radius,
                      the orifice radius.
Discretisation number

All data are in SI units.

"""

from deck import Deck
from machine import RJSMachine
from polymer import Polymer
from models_rjs import *
import numpy
import matplotlib.pyplot as plt

deck = Deck("deck.yaml")
machine = RJSMachine(deck)
polymer = Polymer(deck)

discretisation = int(deck.doc['Discretisation'])
# The higher the discretisation number is, the finer the discretisation will be,
# there will be more points on the graphic.

# Reach machine parameters
name_machine = machine.name
s0 = machine.reservoir_radius
Rc = machine.collector_radius
orifice_radius = machine.orifice_radius

# Reach polymer parameters
name_polymer = polymer.name
rho = polymer.density
mu = polymer.viscosity
surface_tension = polymer.surface_tension

omega_th = critical_rotational_velocity_threshold(surface_tension,
                                                  orifice_radius, s0, rho)
initial_velocity = Initial_velocity(omega_th, s0)

nu = kinematic_viscosity(mu, rho)

omega = numpy.linspace(4000//60, 37000//60, discretisation)

final_radius = []
for k in range(discretisation):
    final_radius.append(final_radius_approx(orifice_radius, initial_velocity,
                                            nu, Rc, omega[k]))
final_radius = numpy.array(final_radius)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for i in range(discretisation):
    axes.plot(omega[i], final_radius[i], 'ro')
axes.grid()
axes.set_xlabel("Angular velocity (rounds per second)", fontsize=16)
axes.set_ylabel("Final radius (m)", fontsize=16)
axes.set_title(" %s / %s " % (name_machine, name_polymer), fontsize=16, y=1.)

# Plot a zoomed graphic on the small radius below 0.00002 m
fig2 = plt.figure()
axes = fig2.add_subplot(1, 1, 1)

for i in range(discretisation-1):
    if final_radius[i] <= 0.00002:
        axes.plot(omega[i], final_radius[i], 'bo')
axes.grid()
axes.set_xlabel("Angular velocity (rounds per second)", fontsize=16)
axes.set_ylabel("Final radius  (m)", fontsize=16)
axes.set_title("ZOOM %s / %s " % (name_machine, name_polymer), fontsize=16, y=1.05)

plt.show()
