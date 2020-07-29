#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from deck import Deck


class RJSMachine:

    # Initializer Attributes
    def __init__(self, deck):
        self.name = deck.doc['Machines']['Name']
        self.orifice_radius = float(deck.doc['Machines']['Orifice Radius'])
        self.collector_radius = float(deck.doc['Machines']['Collector Radius'])
        self.reservoir_radius = float(deck.doc['Machines']['Reservoir Radius'])
        self.omega = float(deck.doc['Machines']['Angular Velocity'])        
