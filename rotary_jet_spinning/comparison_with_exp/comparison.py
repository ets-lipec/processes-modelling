#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:20:47 2020

@author: amelielaurens

Source : [mellado_simple_2011]

Goal : Verify the model by comparing the results obtained with the model and
       the ones obtained with the experiment

Inputs : Concerning the polymer : the surface tension, the density, the viscosity
         Concerning the machine : the collector radius, the orifice radius,
         the angular viscosity of the spinneret
         The initial velocity and the discretisation

All data are in SI units.
"""

import numpy
import matplotlib.pyplot as plt


class Comparison:
    
    def __init__(self, deck, polymer, machine, model, features, experimental):

        self.deck = deck
        self.polymer = polymer
        self.machine = machine
        self.model = model
        self.comparison_with_experiment(deck, polymer, machine, model, features, experimental)


    def comparison_with_experiment(self, deck, polymer, machine, model, features, experimental):
        
        # X Axis : the scaling factor
        scaling_factor = numpy.linspace(1.0, machine.maximum_angular_velocity/machine.mellado_angular_velocity, features.discretisation)
        
        # Y Axis : radius ratio
        radius_ratio = []
        for k in range(features.discretisation):
            Sigma = model.sigma(polymer.mellado_surface_tension, machine.mellado_collector_radius, machine.mellado_orifice_radius, machine.mellado_initial_velocity)
            # Numerator
            r_num = model.radius(machine.mellado_orifice_radius, polymer.mellado_density, machine.mellado_initial_velocity, machine.mellado_collector_radius, polymer.mellado_viscosity, Sigma,
                   scaling_factor[k]*machine.mellado_angular_velocity)
            # Denominator
            r_deno = model.radius(machine.mellado_orifice_radius, polymer.mellado_density, machine.mellado_initial_velocity, machine.mellado_collector_radius, polymer.mellado_viscosity, Sigma,
                    machine.mellado_angular_velocity)
            radius_ratio.append(r_num/r_deno)
        radius_ratio = numpy.array(radius_ratio)
        
        # Plot the figure
        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        
        # Plot the points of the model
        axes.plot(scaling_factor, radius_ratio, 'ro', label='model')
        
        # Plot the points of the experiment
        angular_velocities_exp = experimental.angular_velocities_exp
        scaling_factors_exp = []
        for k in range(len(angular_velocities_exp)):
            scaling_factors_exp.append(float(angular_velocities_exp[k]) / machine.mellado_angular_velocity)
        scaling_factors_exp = numpy.array(scaling_factors_exp)

        radius_ratios = [1.0, 0.88, 0.79, 0.76, 0.69, 0.68, 0.64]
        # When we will get our experimental values we will use the following line instead of the one just above
        # final_radius_exp = experimental.final_radius_exp
        # final_radius_0 = final_radius_exp[0]
        # radius_ratios = []
        # for k in range(len(final_radius_exp)):
        #    radius_ratios.append(float(final_radius_exp[k]) / final_radius_0)
        # radius_ratios = numpy.array(radius_ratios)

        axes.plot(scaling_factors_exp, radius_ratios, 'bx', label='experiment')
        
        axes.grid()
        axes.set_xlabel("Scaling factor", fontsize=16)
        axes.set_ylabel("Radius ratio", fontsize=16)
        axes.set_title("Comparison of the model with experiment", fontsize=16, y=1.)
        axes.legend()
        plt.savefig("./graphics/comparison_with_experiment.pdf", format="pdf")
     