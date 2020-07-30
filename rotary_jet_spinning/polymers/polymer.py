#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Polymer:

    # Initializer Attributes
    def __init__(self, deck):
        self.name = deck.doc['Polymers']['Name']
        self.density = float(deck.doc['Polymers']['Density'])
        self.viscosity = float(deck.doc['Polymers']['Viscosity'])
        self.surface_tension = float(deck.doc['Polymers']['Surface Tension'])
    