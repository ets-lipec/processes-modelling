#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:50:50 2020

@author: amelielaurens

Source : A simple model for nanofiber formation by rotary jet-spinning
by mellado et al.

Goal : Prediction of the critical rotational velocity for jet ejection

Select the machine and the polymer for which we want to run the code.

Inputs : Concerning the polymer : the surface tension, the density
         Concerning the machine : the reservoir radius, the orifice radius.

All data are in SI units.

"""

from deck import Deck
from machine import RJSMachine
from polymer import Polymer
from modelling import RJSModel

deck = Deck("deck.yaml")
machine = RJSMachine(deck)
polymer = Polymer(deck)
model = RJSModel(polymer, machine)

critical_rotational_velocity = model.omega_th

print('The critical rotational velocity threshold for jet ejection is :'
      '%s (in round per second).' % (critical_rotational_velocity))
