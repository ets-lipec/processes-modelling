#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:10:31 2020

@author: amelielaurens

Source : A simple model for nanofiber formation by rotary jet-spinning
by mellado et al.

Goal : Prediction of the radius of the jet in steady state as a function of
the axial coordinate x.

Select the machine and the polymer for which we want to run the code and ajust values
in polymer.yaml and machine.yaml files.

In polymer.yaml : the surface tension, the viscosity, the density
In machine.yaml : the reservoir radius, the collector radius,
                  the orifice radius, the angular viscosity of the spinneret.

All data are in SI units.

"""

from machine import RJSMachine
from polymer import Polymer
from models_rjs import *
import numpy
import matplotlib.pyplot as plt

discretisation = 20
# The higher the discretisation number is, the finer the discretisation will be,
# there will be more points on the graphic.

machine = RJSMachine("machine.yaml")
polymer = Polymer("polymer.yaml")

# Reach machine parameters
name_machine = machine.doc['Machines']['Name']
s0 = float(machine.doc['Machines']['Reservoir Radius'])
Rc = float(machine.doc['Machines']['Collector Radius'])
omega = float(machine.doc['Machines']['Angular Velocity'])
orifice_radius = float(machine.doc['Machines']['Orifice Radius'])

# Reach polymer parameters
name_polymer = polymer.doc['Polymers']['Name']
rho = float(polymer.doc['Polymers']['Density'])
mu = float(polymer.doc['Polymers']['Viscosity'])
surface_tension = float(polymer.doc['Polymers']['Surface Tension'])

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
axes.set_title(" %s / %s " % (name_machine, name_polymer), fontsize=16, y=1.)

# tracer un graphe zoomé sur les petits rayons inférieurs à 0.00010 m
fig2 = plt.figure()
axes = fig2.add_subplot(1, 1, 1)

for i in range(discretisation-1):
    if radius[i] <= 0.00010:
        axes.plot(x_position[i], radius[i], 'bo')
axes.grid()
axes.set_xlabel("Axial coordinate x (m)", fontsize=16)
axes.set_ylabel("Radius (m)", fontsize=16)
axes.set_title("ZOOM %s / %s " % (name_machine, name_polymer), fontsize=16, y=1.05)

plt.show()
