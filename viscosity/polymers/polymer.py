#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Polymer:

    # Initializer Attributes
    def __init__(self, deck):
        self.name = deck.doc['Polymers']['Name']
        self.constantB = float(deck.doc['Polymers']['Constant B'])
        self.constantb = float(deck.doc['Polymers']['Constant b'])
        self.energy = float(deck.doc['Polymers']['Activation Energy'])
    
