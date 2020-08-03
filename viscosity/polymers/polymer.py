#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Polymer:

    # Initializer Attributes
    def __init__(self, deck):
        self.name = deck.doc['Polymers']['Name']
        self.B = float(deck.doc['Polymers']['Constant B'])
        self.b = float(deck.doc['Polymers']['Constant b'])
        self.E = float(deck.doc['Polymers']['Activation Energy'])
    
