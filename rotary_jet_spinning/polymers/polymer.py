#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Polymer:

    # Initializer Attributes
    def __init__(self, deck):
        self.name = deck.doc['Polymers']['Name']
        self.density = float(deck.doc['Polymers']['Density'])
        self.viscosity = float(deck.doc['Polymers']['Viscosity'])
        self.surface_tension = float(deck.doc['Polymers']['Surface Tension'])
        self.kinematic_viscosity = self.viscosity / self.density
        self.minimum_viscosity = float(deck.doc['Range Polymer Parameters']['Minimum Viscosity'])
        self.maximum_viscosity = float(deck.doc['Range Polymer Parameters']['Maximum Viscosity'])
        self.minimum_density = float(deck.doc['Range Polymer Parameters']['Minimum Density'])
        self.maximum_density = float(deck.doc['Range Polymer Parameters']['Maximum Density'])
        self.minimum_surface_tension = float(deck.doc['Range Polymer Parameters']['Minimum Surface Tension'])
        self.maximum_surface_tension = float(deck.doc['Range Polymer Parameters']['Maximum Surface Tension'])
        self.mellado_density = float(deck.doc['Polymers']['Values used by Mellado to compare with experiment']['Density'])
        self.mellado_viscosity = float(deck.doc['Polymers']['Values used by Mellado to compare with experiment']['Viscosity'])
        self.mellado_surface_tension = float(deck.doc['Polymers']['Values used by Mellado to compare with experiment']['Surface Tension'])
