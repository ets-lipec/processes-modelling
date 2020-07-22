#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:48:35 2020

@author: amelielaurens
"""
import yaml, sys
import os.path


class Polymer:

    # Initializer Attributes
    def __init__(self, inputhpath):
        #self.name = name
        #self.density = density
        #self.viscosity = viscosity
        #self.surface_tension = surface_tension
        if not os.path.exists(inputhpath):
            print("File " + inputhpath)
            sys.exit(1)
        else:
            with open(inputhpath,'r') as f:
                ## Container of the tags parsed from the yaml file
                self.doc = yaml.load(f, Loader=yaml.BaseLoader)
