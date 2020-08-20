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
from pandas import DataFrame


class Data:
    
    def __init__(self, deck, polymer, machine, model, features):
        
        self.deck = deck
        self.polymer = polymer
        self.machine = machine
        self.model = model
        self.final_radius_orifice_radius(deck, polymer, machine, model, features)
        self.final_radius_angular_velocity(deck, polymer, machine, model, features)
        self.final_radius_collector_radius(deck, polymer, machine, model, features)
        self.final_radius_reservoir_radius(deck, polymer, machine, model, features)
        self.final_radius_density(deck, polymer, machine, model, features)
        self.final_radius_surface_tension(deck, polymer, machine, model, features)
        self.final_radius_viscosity(deck, polymer, machine, model, features)
        self.radius_x(deck, polymer, machine, model, features)
        


    def final_radius_orifice_radius(self, deck, polymer, machine, model, features):
        # Prediction of the final fiber radius for various orifice radius
        
        orifice_radius = numpy.linspace(machine.minimum_orifice_radius, machine.maximum_orifice_radius, features.discretisation)
        orifice_radius = orifice_radius.tolist()
        
        omega_th = []
        init_velocity = []
        for l in range(features.discretisation):
            omega_th.append(model.critical_rotational_velocity_threshold(polymer.surface_tension, orifice_radius[l],
                                                           machine.reservoir_radius, polymer.density))
            init_velocity.append(model.initial_velocity(omega_th[l], machine.reservoir_radius))
        
        Final_radius = []
        for k in range(features.discretisation):
            Final_radius.append(model.final_radius(orifice_radius[k], init_velocity[k],
                                            polymer.kinematic_viscosity, machine.collector_radius, machine.angular_velocity))

        # Put data in a dictionary
        dictData = {'Orifice radius': orifice_radius, 'Final fiber radius': Final_radius}
        dataFrm = DataFrame(dictData, columns= ['Orifice radius', 'Final fiber radius'])
        # Store the data in a file .csv in the folder data_files
        export_csv = dataFrm .to_csv (r'./data_files/PandaOrificeRadius.csv', index = None, header=False)

        return [orifice_radius, Final_radius]


    
    def final_radius_angular_velocity(self, deck, polymer, machine, model, features):
        # Prediction of the final fiber radius for various angular velocities
        
        omega_th = model.critical_rotational_velocity_threshold(polymer.surface_tension,
                                                  machine.orifice_radius, machine.reservoir_radius, polymer.density)
                                                  
        init_velocity = model.initial_velocity(omega_th, machine.reservoir_radius)
        
        omega = numpy.linspace(machine.minimum_angular_velocity, machine.maximum_angular_velocity, features.discretisation)
        omega = omega.tolist()
        
        Final_radius = []
        for k in range(features.discretisation):
            Final_radius.append(model.final_radius(machine.orifice_radius, init_velocity,
                                            polymer.kinematic_viscosity, machine.collector_radius, omega[k]))
        
        # Put data in a dictionary
        dictData = {'Angular Velocity': omega, 'Final fiber radius': Final_radius}
        dataFrm = DataFrame(dictData, columns= ['Angular Velocity', 'Final fiber radius'])
        # Store the data in a file .csv in the folder data_files
        export_csv = dataFrm .to_csv (r'./data_files/PandaAngularVelocity.csv', index = None, header=False)

        return [omega, Final_radius]

        
        
    def final_radius_collector_radius(self, deck, polymer, machine, model, features):
        # Prediction of the final fiber radius for various collector distances

        omega_th = model.critical_rotational_velocity_threshold(polymer.surface_tension,
                                                  machine.orifice_radius, machine.reservoir_radius, polymer.density)
                                                  
        init_velocity = model.initial_velocity(omega_th, machine.reservoir_radius)
        
        Rc = numpy.linspace(machine.minimum_collector_radius, machine.maximum_collector_radius, features.discretisation)
        Rc = Rc.tolist()
        
        Final_radius = []
        for k in range(features.discretisation):
            Final_radius.append(model.final_radius(machine.orifice_radius, init_velocity,
                                            polymer.kinematic_viscosity, Rc[k], machine.angular_velocity))

        # Put data in a dictionary
        dictData = {'Collector Radius': Rc, 'Final fiber radius': Final_radius}
        dataFrm = DataFrame(dictData, columns= ['Collector Radius', 'Final fiber radius'])
        # Store the data in a file .csv in the folder data_files
        export_csv = dataFrm .to_csv (r'./data_files/PandaCollectorRadius.csv', index = None, header=False)

        return [Rc, Final_radius]
        

    
    def final_radius_reservoir_radius(self, deck, polymer, machine, model, features):
        # Prediction of the final fiber radius for various reservoir radius

        s0 = numpy.linspace(machine.minimum_reservoir_radius, machine.maximum_reservoir_radius, features.discretisation)
        s0 = s0.tolist()
        
        omega_th = []
        init_velocity = []
        for l in range(features.discretisation):
            omega_th.append(model.critical_rotational_velocity_threshold(polymer.surface_tension,
                                                           machine.orifice_radius, s0[l], polymer.density))
            init_velocity.append(model.initial_velocity(omega_th[l], s0[l]))
        
        Final_radius = []
        for k in range(features.discretisation):
            Final_radius.append(model.final_radius(machine.orifice_radius, init_velocity[k],
                                            polymer.kinematic_viscosity, machine.collector_radius, machine.angular_velocity))

        # Put data in a dictionary
        dictData = {'Reservoir Radius': s0, 'Final fiber radius': Final_radius}
        dataFrm = DataFrame(dictData, columns= ['Reservoir Radius', 'Final fiber radius'])
        # Store the data in a file .csv in the folder data_files
        export_csv = dataFrm .to_csv (r'./data_files/PandaReservoirRadius.csv', index = None, header=False)

        return [s0, Final_radius]

        

    def final_radius_density(self, deck, polymer, machine, model, features):
        # Prediction of the final fiber radius for various polymer density

        rho = numpy.linspace(polymer.minimum_density, polymer.maximum_density, features.discretisation)
        rho = rho.tolist()

        omega_th = []
        init_velocity = []
        nu = []
        for l in range(features.discretisation):
            omega_th.append(model.critical_rotational_velocity_threshold(polymer.surface_tension,
                                                  machine.orifice_radius, machine.reservoir_radius, rho[l]))
            init_velocity.append(model.initial_velocity(omega_th[l], machine.reservoir_radius))
            nu.append(model.kinematic_viscosity(polymer.viscosity, rho[l]))
        
        Final_radius = []
        for k in range(features.discretisation):
            Final_radius.append(model.final_radius(machine.orifice_radius, init_velocity[k], nu[k],
                                                   machine.collector_radius, machine.angular_velocity))

        # Put data in a dictionary
        dictData = {'Density': rho, 'Final fiber radius': Final_radius}
        dataFrm = DataFrame(dictData, columns= ['Density', 'Final fiber radius'])
        # Store the data in a file .csv in the folder data_files
        export_csv = dataFrm .to_csv (r'./data_files/PandaDensity.csv', index = None, header=False)

        return [rho, Final_radius]

        

    def final_radius_surface_tension(self, deck, polymer, machine, model, features):
        # Prediction of the final fiber radius for various polymer surface tension

        surface_tension = numpy.linspace(polymer.minimum_surface_tension, polymer.maximum_surface_tension, features.discretisation)
        surface_tension = surface_tension.tolist()

        omega_th = []
        init_velocity = []
        for l in range(features.discretisation):
            omega_th.append(model.critical_rotational_velocity_threshold(surface_tension[l], machine.orifice_radius,
                                                                 machine.reservoir_radius, polymer.density))
            init_velocity.append(model.initial_velocity(omega_th[l], machine.reservoir_radius))
        
        Final_radius = []
        for k in range(features.discretisation):
            Final_radius.append(model.final_radius(machine.orifice_radius, init_velocity[k],
                                            polymer.kinematic_viscosity, machine.collector_radius, machine.angular_velocity))

        # Put data in a dictionary
        dictData = {'Surface Tension': surface_tension, 'Final fiber radius': Final_radius}
        dataFrm = DataFrame(dictData, columns= ['Surface Tension', 'Final fiber radius'])
        # Store the data in a file .csv in the folder data_files
        export_csv = dataFrm .to_csv (r'./data_files/PandaSurfaceTension.csv', index = None, header=False)

        return [surface_tension, Final_radius]


    
    def final_radius_viscosity(self, deck, polymer, machine, model, features):
        # Prediction of the final fiber radius for various polymer viscosity

        mu = numpy.linspace(polymer.minimum_viscosity, polymer.maximum_viscosity, features.discretisation)
        mu = mu.tolist()
        
        omega_th = model.critical_rotational_velocity_threshold(polymer.surface_tension,
                                                  machine.orifice_radius, machine.reservoir_radius, polymer.density)
        
        init_velocity = model.initial_velocity(omega_th, machine.reservoir_radius)
        
        nu = []
        for l in range(features.discretisation):
            nu.append(model.kinematic_viscosity(mu[l], polymer.density))
        
        Final_radius = []
        for k in range(features.discretisation):
            Final_radius.append(model.final_radius(machine.orifice_radius, init_velocity,
                                            nu[k], machine.collector_radius, machine.angular_velocity))

        # Put data in a dictionary
        dictData = {'Viscosity': mu, 'Final fiber radius': Final_radius}
        dataFrm = DataFrame(dictData, columns= ['Viscosity', 'Final fiber radius'])
        # Store the data in a file .csv in the folder data_files
        export_csv = dataFrm .to_csv (r'./data_files/PandaViscosity.csv', index = None, header=False)

        return [mu, Final_radius]
        


    def radius_x(self, deck, polymer, machine, model, features):
        # Prediction of the radius of the jet in steady state as a function of
        # the axial coordinate x

        x_position = numpy.linspace(machine.reservoir_radius, machine.collector_radius-machine.reservoir_radius, features.discretisation)
        x_position = x_position.tolist()

        omega_th = model.critical_rotational_velocity_threshold(polymer.surface_tension,
                                                  machine.orifice_radius, machine.reservoir_radius, polymer.density)
                                                  
        init_velocity = model.initial_velocity(omega_th, machine.reservoir_radius)
        
        Sigma = []
        for l in range(features.discretisation):
            Sigma.append(model.sigma(polymer.surface_tension, x_position[l], machine.orifice_radius,
                       init_velocity))
        
        Radius = []
        for k in range(features.discretisation):
            Radius.append(model.radius(machine.orifice_radius, polymer.density, init_velocity, x_position[k], polymer.viscosity, Sigma[k], machine.angular_velocity))

        # Put data in a dictionary
        dictData = {'Axial Coordinate x': x_position, 'Fiber radius': Radius}
        dataFrm = DataFrame(dictData, columns= ['Axial Coordinate x', 'Fiber radius'])
        # Store the data in a file .csv in the folder data_files
        export_csv = dataFrm .to_csv (r'./data_files/PandaAxialCoordinate.csv', index = None, header=False)

        return [x_position, Radius]
        