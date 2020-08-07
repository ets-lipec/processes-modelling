#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class RJSMachine:

    # Initializer Attributes
    def __init__(self, deck):
        self.name = deck.doc['Machines']['Name']
        self.orifice_radius = float(deck.doc['Machines']['Orifice Radius'])
        self.collector_radius = float(deck.doc['Machines']['Collector Radius'])
        self.reservoir_radius = float(deck.doc['Machines']['Reservoir Radius'])
        self.angular_velocity = float(deck.doc['Machines']['Angular Velocity'])
        self.minimum_orifice_radius = float(deck.doc['Range Machine Parameters']['Minimum Orifice Radius'])
        self.maximum_orifice_radius = float(deck.doc['Range Machine Parameters']['Maximum Orifice Radius']) 
        self.minimum_collector_radius = float(deck.doc['Range Machine Parameters']['Minimum Collector Radius']) 
        self.maximum_collector_radius = float(deck.doc['Range Machine Parameters']['Maximum Collector Radius']) 
        self.minimum_reservoir_radius = float(deck.doc['Range Machine Parameters']['Minimum Reservoir Radius']) 
        self.maximum_reservoir_radius = float(deck.doc['Range Machine Parameters']['Maximum Reservoir Radius']) 
        self.minimum_angular_velocity = float(deck.doc['Range Machine Parameters']['Minimum Angular Velocity']) 
        self.maximum_angular_velocity = float(deck.doc['Range Machine Parameters']['Maximum Angular Velocity'])      
