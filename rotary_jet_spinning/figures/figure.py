#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Source : A simple model for nanofiber formation by rotary jet-spinning
by mellado et al.

Goal : Prediction of the radius of the fiber

Change values of the machine and the polymer for which we want to run the code in deck.yaml.

Inputs : Concerning the polymer : the surface tension, the density, the viscosity
         Concerning the machine : the reservoir radius, the collector radius,
                                  the orifice radius,
                                  the angular viscosity of the spinneret.

All data are in SI units.

"""


import numpy
import matplotlib.pyplot as plt


class Graph:
    
    def __init__(self, deck, polymer, machine, model):
        
        self.deck = deck
        self.polymer = polymer
        self.machine = machine
        self.model = model
        self.final_radius_orifice_radius(deck, polymer, machine, model)
        self.final_radius_omega(deck, polymer, machine, model)
        self.final_radius_collector_radius(deck, polymer, machine, model)
        self.final_radius_reservoir_radius(deck, polymer, machine, model)
        self.final_radius_density(deck, polymer, machine, model)
        self.final_radius_surface_tension(deck, polymer, machine, model)
        self.final_radius_viscosity(deck, polymer, machine, model)
        self.radius_x(deck, polymer, machine, model)
        


    def final_radius_orifice_radius(self, deck, polymer, machine, model):
        
        discretisation = int(deck.doc['Discretisation'])
        # The higher the discretisation number is, the finer the discretisation will be,
        # there will be more points on the graphic.
        
        orifice_radius = numpy.linspace(0.0001, 0.001, discretisation)
        
        omega_th = []
        initial_velocity = []
        for l in range(discretisation):
            omega_th.append(model.critical_rotational_velocity_threshold(polymer.surface_tension, orifice_radius[l],
                                                           machine.reservoir_radius, polymer.density))
            initial_velocity.append(model.Initial_velocity(omega_th[l], machine.reservoir_radius))
        omega_th = numpy.array(omega_th)
        initial_velocity = numpy.array(initial_velocity)
        
        nu = model.kinematic_viscosity(polymer.viscosity, polymer.density)
        
        Final_radius = []
        for k in range(discretisation):
            Final_radius.append(model.final_radius(orifice_radius[k], initial_velocity[k],
                                            nu, machine.collector_radius, machine.omega))
        Final_radius = numpy.array(Final_radius)
        
        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        axes.plot(orifice_radius, Final_radius, 'ro')
        axes.grid()
        axes.set_xlabel("Radius of the orifice (m)", fontsize=16)
        axes.set_ylabel("Final radius (m)", fontsize=16)
        axes.set_title(" %s / %s " % (machine.name, polymer.name), fontsize=16, y=1.)
        plt.savefig("./graphics/final_radius_orifice_radius.pdf", format="pdf")

    
    def final_radius_omega(self, deck, polymer, machine, model):
        
        discretisation = int(deck.doc['Discretisation'])
        # The higher the discretisation number is, the finer the discretisation will be,
        # there will be more points on the graphic.
        
        omega_th = model.critical_rotational_velocity_threshold(polymer.surface_tension,
                                                  machine.orifice_radius, machine.reservoir_radius, polymer.density)
                                                  
        initial_velocity = model.Initial_velocity(omega_th, machine.reservoir_radius)
        
        nu = model.kinematic_viscosity(polymer.viscosity, polymer.density)
        
        omega = numpy.linspace(2000//60, 37000//60, discretisation)
        
        Final_radius = []
        for k in range(discretisation):
            Final_radius.append(model.final_radius(machine.orifice_radius, initial_velocity,
                                            nu, machine.collector_radius, omega[k]))
        Final_radius = numpy.array(Final_radius)
        
        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        axes.plot(omega, Final_radius, 'ro')
        axes.grid()
        axes.set_xlabel("Angular velocity (rounds per second)", fontsize=16)
        axes.set_ylabel("Final radius (m)", fontsize=16)
        axes.set_title(" %s / %s " % (machine.name, polymer.name), fontsize=16, y=1.)
        plt.savefig("./graphics/final_radius_omega.pdf", format="pdf")
        
        
    def final_radius_collector_radius(self, deck, polymer, machine, model):
        
        discretisation = int(deck.doc['Discretisation'])
        # The higher the discretisation number is, the finer the discretisation will be,
        # there will be more points on the graphic.

        omega_th = model.critical_rotational_velocity_threshold(polymer.surface_tension,
                                                  machine.orifice_radius, machine.reservoir_radius, polymer.density)
                                                  
        initial_velocity = model.Initial_velocity(omega_th, machine.reservoir_radius)
        
        nu = model.kinematic_viscosity(polymer.viscosity, polymer.density)
        
        Rc = numpy.linspace(0.1, 0.5, discretisation)
        
        Final_radius = []
        for k in range(discretisation):
            Final_radius.append(model.final_radius(machine.orifice_radius, initial_velocity,
                                            nu, Rc[k], machine.omega))
        Final_radius = numpy.array(Final_radius)
        
        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        axes.plot(Rc, Final_radius, 'ro')
        axes.grid()
        axes.set_xlabel("Collector distance (m)", fontsize=16)
        axes.set_ylabel("Final radius (m)", fontsize=16)
        axes.set_title(" %s / %s " % (machine.name, polymer.name), fontsize=16, y=1.)
        plt.savefig("./graphics/final_radius_collector_radius.pdf", format="pdf")

    
    def final_radius_reservoir_radius(self, deck, polymer, machine, model):
        
        discretisation = int(deck.doc['Discretisation'])
        # The higher the discretisation number is, the finer the discretisation will be,
        # there will be more points on the graphic

        s0 = numpy.linspace(0.01, 0.1, discretisation)
        
        omega_th = []
        initial_velocity = []
        for l in range(discretisation):
            omega_th.append(model.critical_rotational_velocity_threshold(polymer.surface_tension,
                                                           machine.orifice_radius, s0[l], polymer.density))
            initial_velocity.append(model.Initial_velocity(omega_th[l], s0[l]))
        omega_th = numpy.array(omega_th)
        initial_velocity = numpy.array(initial_velocity)
        
        nu = model.kinematic_viscosity(polymer.viscosity, polymer.density)
        
        Final_radius = []
        for k in range(discretisation):
            Final_radius.append(model.final_radius(machine.orifice_radius, initial_velocity[k],
                                            nu, machine.collector_radius, machine.omega))
        Final_radius = numpy.array(Final_radius)
        
        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        axes.plot(s0, Final_radius, 'ro')
        axes.grid()
        axes.set_xlabel("Radius of the reservoir (m)", fontsize=16)
        axes.set_ylabel("Final radius (m)", fontsize=16)
        axes.set_title(" %s / %s " % (machine.name, polymer.name), fontsize=16, y=1.)
        plt.savefig("./graphics/final_radius_reservoir_radius.pdf", format="pdf")


    def final_radius_density(self, deck, polymer, machine, model):
        
        discretisation = int(deck.doc['Discretisation'])
        # The higher the discretisation number is, the finer the discretisation will be,
        # there will be more points on the graphic

        rho = numpy.linspace(900, 1500, discretisation)
        
        omega_th = []
        initial_velocity = []
        nu = []
        for l in range(discretisation):
            omega_th.append(model.critical_rotational_velocity_threshold(polymer.surface_tension,
                                                  machine.orifice_radius, machine.reservoir_radius, rho[l]))
            initial_velocity.append(model.Initial_velocity(omega_th[l], machine.reservoir_radius))
            nu.append(model.kinematic_viscosity(polymer.viscosity, rho[l]))
        omega_th = numpy.array(omega_th)
        initial_velocity = numpy.array(initial_velocity)
        nu = numpy.array(nu)
        
        Final_radius = []
        for k in range(discretisation):
            Final_radius.append(model.final_radius(machine.orifice_radius, initial_velocity[k], nu[k],
                                                   machine.collector_radius, machine.omega))
        Final_radius = numpy.array(Final_radius)
        
        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        axes.plot(rho, Final_radius, 'ro')
        axes.grid()
        axes.set_xlabel("Density (kg/m^3)", fontsize=16)
        axes.set_ylabel("Final radius (m)", fontsize=16)
        axes.set_title(" %s / %s " % (machine.name, polymer.name), fontsize=16, y=1.)
        plt.savefig("./graphics/final_radius_density.pdf", format="pdf")


    def final_radius_surface_tension(self, deck, polymer, machine, model):
        
        discretisation = int(deck.doc['Discretisation'])
        # The higher the discretisation number is, the finer the discretisation will be,
        # there will be more points on the graphic

        surface_tension = numpy.linspace(0.02, 0.06, discretisation)
        
        omega_th = []
        initial_velocity = []
        for l in range(discretisation):
            omega_th.append(model.critical_rotational_velocity_threshold(surface_tension[l], machine.orifice_radius,
                                                                 machine.reservoir_radius, polymer.density))
            initial_velocity.append(model.Initial_velocity(omega_th[l], machine.reservoir_radius))
        omega_th = numpy.array(omega_th)
        initial_velocity = numpy.array(initial_velocity)
        
        nu = model.kinematic_viscosity(polymer.viscosity, polymer.density)
        
        Final_radius = []
        for k in range(discretisation):
            Final_radius.append(model.final_radius(machine.orifice_radius, initial_velocity[k],
                                            nu, machine.collector_radius, machine.omega))
        Final_radius = numpy.array(Final_radius)
        
        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        axes.plot(surface_tension, Final_radius, 'ro')
        axes.grid()
        axes.set_xlabel("Surface tension (kg/s^2)", fontsize=16)
        axes.set_ylabel("Final radius (m)", fontsize=16)
        axes.set_title(" %s / %s " % (machine.name, polymer.name), fontsize=16, y=1.)
        plt.savefig("./graphics/final_radius_surface_tension.pdf", format="pdf")
    
    
    def final_radius_viscosity(self, deck, polymer, machine, model):
        
        discretisation = int(deck.doc['Discretisation'])
        # The higher the discretisation number is, the finer the discretisation will be,
        # there will be more points on the graphic

        mu = numpy.linspace(0.1, 1.0, discretisation)
        
        omega_th = model.critical_rotational_velocity_threshold(polymer.surface_tension,
                                                  machine.orifice_radius, machine.reservoir_radius, polymer.density)
        
        initial_velocity = model.Initial_velocity(omega_th, machine.reservoir_radius)
        
        nu = []
        for l in range(discretisation):
            nu.append(model.kinematic_viscosity(mu[l], polymer.density))
        nu = numpy.array(nu)
        
        Final_radius = []
        for k in range(discretisation):
            Final_radius.append(model.final_radius(machine.orifice_radius, initial_velocity,
                                            nu[k], machine.collector_radius, machine.omega))
        Final_radius = numpy.array(Final_radius)
        
        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        axes.plot(nu, Final_radius, 'ro')
        axes.grid()
        axes.set_xlabel("Polymer viscosity (Pa.s)", fontsize=16)
        axes.set_ylabel("Final radius (m)", fontsize=16)
        axes.set_title(" %s / %s " % (machine.name, polymer.name), fontsize=16, y=1.)
        plt.savefig("./graphics/final_radius_viscosity.pdf", format="pdf")



    def radius_x(self, deck, polymer, machine, model):

        discretisation = int(deck.doc['Discretisation'])
        # The higher the discretisation number is, the finer the discretisation will be,
        # there will be more points on the graphic

        x_position = numpy.linspace(machine.reservoir_radius, machine.collector_radius-machine.reservoir_radius, discretisation)
        
        omega_th = model.critical_rotational_velocity_threshold(polymer.surface_tension,
                                                  machine.orifice_radius, machine.reservoir_radius, polymer.density)
                                                  
        initial_velocity = model.Initial_velocity(omega_th, machine.reservoir_radius)
        
        Sigma = []
        for l in range(discretisation):
            Sigma.append(model.sigma(polymer.surface_tension, x_position[l], machine.orifice_radius,
                       initial_velocity))
        Sigma = numpy.array(Sigma)
        
        Radius = []
        for k in range(discretisation):
            Radius.append(model.radius(machine.orifice_radius, polymer.density, initial_velocity, x_position[k],
                         polymer.viscosity, Sigma[k], machine.omega))
        Radius = numpy.array(Radius)
        
        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        axes.plot(x_position, Radius, 'ro')
        axes.grid()
        axes.set_xlabel("Axial coordinate x (m)", fontsize=16)
        axes.set_ylabel("Radius (m)", fontsize=16)
        axes.set_title(" %s / %s " % (machine.name, polymer.name), fontsize=16, y=1.)
        plt.savefig("./graphics/radius_x.pdf", format="pdf")
