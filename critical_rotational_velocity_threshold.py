#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:50:50 2020

@author: amelielaurens

Source : A simple model for nanofiber formation by rotary jet-spinning
by mellado et al.

Goal : Prediction of the critical rotational velocity for jet ejection

Select the machine and the polymer for which we want to run the code and ajust values
in polymer.yaml and machine.yaml files.

In polymer.yaml : the surface tension, the density
In machine.yaml : the reservoir radius, the orifice radius.

All data are in SI units.

"""
c
from machine import RJSMachine
from polymer import Polymer
from models_rjs import *

machine = RJSMachine("machine.yaml")
polymer = Polymer("polymer.yaml")

# Reach machine parameters
name_machine = machine.doc['Machines']['Name']
s0 = float(machine.doc['Machines']['Reservoir Radius'])
orifice_radius = float(machine.doc['Machines']['Orifice Radius'])

# Reach polymer parameters
name_polymer = polymer.doc['Polymers']['Name']
surface_tension = float(polymer.doc['Polymers']['Surface Tension'])
rho = float(polymer.doc['Polymers']['Density'])# Choose one machine and one polymer

critical_rotational_velocity = critical_rotational_velocity_threshold(surface_tension,
                                                                      orifice_radius, s0, rho)
print('The critical rotational velocity threshold for jet ejection is :'
      '%s (in round per second).' % (critical_rotational_velocity))
