#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:48:35 2020

@author: amelielaurens
"""
from deck import Deck


class Polymer:

    # Initializer Attributes
    def __init__(self, deck = Deck("deck.yaml")):
        self.name = deck.doc['Polymers']['Name']
        self.density = float(deck.doc['Polymers']['Density'])
        self.viscosity = float(deck.doc['Polymers']['Viscosity'])
        self.surface_tension = float(polymer.doc['Polymers']['Surface Tension'])
