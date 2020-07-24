#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:20:47 2020

@author: amelielaurens

Source : A simple model for nanofiber formation by rotary jet-spinning
by mellado et al.

Goal : Verify the model by comparing the results obtained with the model and
       the ones obtained with the experiment

Inputs : Concerning the polymer : the surface tension, the density, the viscosity
         Concerning the machine : the collector radius, the orifice radius,
         the angular viscosity of the spinneret
         The initial velocity and the discretisation

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
model = RJSModel(deck, polymer, machine)

discretisation = int(deck.doc['Discretisation'])
# The higher the discretisation number is, the finer the discretisation will be,
# there will be more points on the graphic.

# Values used by Mellado
Rc = 0.135
rho = 1540
surface_tension = 0.027
initial_velocity = 0.1
orifice_radius = 0.000170
mu = 0.113
omega = 200

# X Axis : the scaling factor
scaling_factor = numpy.linspace(1.0, 2.6, discretisation)

# Y Axis : radius ratio
radius_ratio = []
for k in range(discretisation):
    Sigma = model.sigma(surface_tension, Rc, orifice_radius, initial_velocity)
    # Numerator
    r_num = model.radius(orifice_radius, rho, initial_velocity, Rc, mu, Sigma,
                   scaling_factor[k]*omega)
    # Denominator
    r_deno = model.radius(orifice_radius, rho, initial_velocity, Rc, mu, Sigma,
                    omega)
    radius_ratio.append(r_num/r_deno)
radius_ratio = numpy.array(radius_ratio)

# Plot the figure
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

# Plot the points of the model
axes.plot(scaling_factor, radius_ratio, 'ro', label='model')

# Plot the points of the experiment
x = [1.0, 1.1, 1.3, 1.5, 1.8, 2.1, 2.4]
y = [1.0, 0.88, 0.79, 0.76, 0.69, 0.68, 0.64]

axes.plot(x, y, 'bx', label='experiment')

axes.grid()
axes.set_xlabel("Scaling factor", fontsize=16)
axes.set_ylabel("Radius ratio", fontsize=16)
axes.set_title("Comparison of the model with experiment", fontsize=16, y=1.)

axes.legend()
plt.show()
