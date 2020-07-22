#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:38:23 2020

@author: amelielaurens
"""
import yaml, sys
import os.path


class RJSMachine:

    # Initializer Attributes
    def __init__(self, inputhpath):
        #self.name = name
        #self.orifice_radius = orifice_radius
        #self.collector_radius = collector_radius
        #self.reservoir_radius = reservoir_radius
        #self.omega = omega
        if not os.path.exists(inputhpath):
            print("File " + inputhpath)
            sys.exit(1)
        else:
            with open(inputhpath,'r') as f:
                ## Container of the tags parsed from the yaml file
                self.doc = yaml.load(f, Loader=yaml.BaseLoader)
        