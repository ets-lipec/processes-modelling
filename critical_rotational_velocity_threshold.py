#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:50:50 2020

@author: amelielaurens

Source : A simple model for nanofiber formation by rotary jet-spinning
by mellado et al.

Goal : Prediction of the critical rotational velocity for jet ejection

Select the machine and the polymer for which we want to run the code and ajust values
in deck.yaml file.

Polymer parameters : the density, the surface tension
Machine parameters  : the reservoir radius, the orifice radius

All data are in SI units.

"""

from deck import Deck
from machine import RJSMachine
from polymer import Polymer
from models_rjs import *

deck = Deck("deck.yaml")
machine = RJSMachine(deck)
polymer = Polymer(deck)

# Reach machine parameters
name_machine = machine.name
s0 = machine.reservoir_radius
orifice_radius = machine.orifice_radius

# Reach polymer parameters
name_polymer = polymer.name
rho = polymer.density
surface_tension = polymer.surface_tension

critical_rotational_velocity = critical_rotational_velocity_threshold(surface_tension,
                                                                      orifice_radius, s0, rho)
print('The critical rotational velocity threshold for jet ejection is :'
      '%s (in round per second).' % (critical_rotational_velocity))
