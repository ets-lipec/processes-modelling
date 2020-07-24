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

from deck import Deck
from machine import RJSMachine
from polymer import Polymer
from modelling import RJSModel
import numpy
import matplotlib.pyplot as plt

deck = Deck("deck.yaml")
machine = RJSMachine(deck)
polymer = Polymer(deck)
model = RJSModel(polymer, machine)

discretisation = 20
# The higher the discretisation number is, the finer the discretisation will be,
# there will be more points on the graphic.

# Reach machine parameters
name_machine = machine.name
s0 = machine.reservoir_radius
Rc = machine.collector_radius
omega = machine.omega
orifice_radius = machine.orifice_radius

# Reach polymer parameters
name_polymer = polymer.name
rho = polymer.density
mu = polymer.viscosity
surface_tension = polymer.surface_tension

x_position = numpy.linspace(0, Rc-s0, discretisation)

omega_th = model.critical_rotational_velocity_threshold(surface_tension,
                                                  orifice_radius, s0, rho)
initial_velocity = model.Initial_velocity(omega_th, s0)
Sigma = []
for l in range(discretisation):
    Sigma.append(model.sigma(surface_tension, x_position[l], orifice_radius,
                       initial_velocity))
Sigma = numpy.array(Sigma)

Radius = []
for k in range(1, discretisation):
    Radius.append(model.radius(orifice_radius, rho, initial_velocity, x_position[k],
                         mu, Sigma[k], omega))
Radius = numpy.array(Radius)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for i in range(discretisation-1):
    axes.plot(x_position[i], Radius[i], 'ro')
axes.grid()
axes.set_xlabel("Axial coordinate x (m)", fontsize=16)
axes.set_ylabel("Radius (m)", fontsize=16)
axes.set_title(" %s / %s " % (name_machine, name_polymer), fontsize=16, y=1.)

# Plot a zoomed graphic on the small radius below 0.00002 m
fig2 = plt.figure()
axes = fig2.add_subplot(1, 1, 1)

for i in range(discretisation-1):
    if Radius[i] <= 0.00002:
        axes.plot(x_position[i], Radius[i], 'bo')
axes.grid()
axes.set_xlabel("Axial coordinate x (m)", fontsize=16)
axes.set_ylabel("Radius (m)", fontsize=16)
axes.set_title("ZOOM %s / %s " % (name_machine, name_polymer), fontsize=16, y=1.05)

plt.show()
