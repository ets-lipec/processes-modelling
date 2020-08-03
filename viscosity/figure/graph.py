#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt
from math import *


class Graph:
    
    def __init__(self, deck, polymer, model):
        
        self.deck = deck
        self.polymer = polymer
        self.model = model
        self.viscosity_as_a_function_of_temperature_and_shear_stress(deck, polymer, model)
    
        

    def viscosity_as_a_function_of_temperature_and_shear_stress(self, deck, polymer, model):

        discretisation = int(deck.doc['Discretisation'])
        # The higher the discretisation number is, the finer the discretisation will be,
        # there will be more points on the graphic.
        
        T = [463, 483, 503, 533, 553]
        T = numpy.array(T)
        color = ['ro', 'bo', 'go', 'yo', 'ko']
        legend = ['463K', '483K', '503K', '533K', '553K']
        
        shear_stress_power = numpy.linspace(250, 1000, discretisation)
        
        R = float(deck.doc['Constants']['Gas Constant'])


        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        
        for k in range(len(T)):
            log_melt_viscosity = []
            for i in range(discretisation):
                melt_viscosity = model.viscosity(polymer.constantB, polymer.energy, R, T[k], polymer.constantb, shear_stress_power[i])
                log_melt_viscosity.append(log10(melt_viscosity))
            log_melt_viscosity = numpy.array(log_melt_viscosity)
            axes.plot(shear_stress_power, log_melt_viscosity, color[k], label = legend[k])
            
        axes.grid()
        axes.set_xlabel("Shear stress to the power of 1/2", fontsize=16)
        axes.set_ylabel("log ( Melt viscosity )", fontsize=16)
        axes.set_title(" %s " % (polymer.name), fontsize=16, y=1.)
        axes.legend()
        plt.savefig("./graphics/viscosity_as_a_function_of_temperature_and_shear_stress.pdf", format="pdf")
