#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Organization:

    def __init__(self, data, deck, machine, polymer, model, features):
        self.data = data
        self.deck = deck
        self.machine = machine
        self.polymer = polymer
        self.model = model
        self.organize_data(data, deck, machine, polymer, model, features)
    

    def organize_data(self, data, deck, machine, polymer, model, features):
        
        organized_data = [{"x": data.final_radius_orifice_radius(deck, polymer, machine, model, features)[0],
                "x_legend": "Radius of the orifice (m)",
                "y": data.final_radius_orifice_radius(deck, polymer, machine, model, features)[1],
                "y_legend" : "Final fiber radius (m)", "color": "ro",
                "title": " %s / %s " % (machine.name, polymer.name),
                "save_as": "./graphics/final_radius_orifice_radius.pdf",
                "panda_file_title" : "./data_files/PandaOrificeRadius.csv"}] 
                
        organized_data.append({"x": data.final_radius_angular_velocity(deck, polymer, machine, model, features)[0],
                     "x_legend": "Angular velocity (rounds per second)",
                     "y": data.final_radius_angular_velocity(deck, polymer, machine, model, features)[1],
                     "y_legend" : "Final fiber radius (m)", "color": "bo",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/final_radius_angular_velocity.pdf",
                     "panda_file_title" : "./data_files/PandaAngularVelocity.csv"})
                     
        organized_data.append({"x": data.final_radius_collector_radius(deck, polymer, machine, model, features)[0],
                     "x_legend": "Collector distance (m)",
                     "y": data.final_radius_collector_radius(deck, polymer, machine, model, features)[1],
                     "y_legend" : "Final fiber radius (m)", "color": "go",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/final_radius_collector_radius.pdf",
                     "panda_file_title" : "./data_files/PandaCollectorRadius.csv"})
                     
        organized_data.append({"x": data.final_radius_reservoir_radius(deck, polymer, machine, model, features)[0],
                     "x_legend": "Radius of the reservoir (m)",
                     "y": data.final_radius_reservoir_radius(deck, polymer, machine, model, features)[1],
                     "y_legend" : "Final fiber radius (m)", "color": "yo",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/final_radius_reservoir_radius.pdf",
                     "panda_file_title" : "./data_files/PandaReservoirRadius.csv"})
                     
        organized_data.append({"x": data.final_radius_density(deck, polymer, machine, model, features)[0],
                     "x_legend": "Density (kg/m^3)",
                     "y": data.final_radius_density(deck, polymer, machine, model, features)[1],
                     "y_legend" : "Final fiber radius (m)", "color": "ko",
                     "title": " %s / %s " % (machine.name, polymer.name),
                    "save_as": "./graphics/final_radius_density.pdf",
                    "panda_file_title" : "./data_files/PandaDensity.csv"})
                    
        organized_data.append({"x": data.final_radius_surface_tension(deck, polymer, machine, model, features)[0],
                     "x_legend": "Surface tension (kg/s^2)",
                     "y": data.final_radius_surface_tension(deck, polymer, machine, model, features)[1],
                     "y_legend" : "Final fiber radius (m)", "color": "mo",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/final_radius_surface_tension.pdf",
                     "panda_file_title" : "./data_files/PandaSurfaceTension.csv"})
                     
        organized_data.append({"x": data.final_radius_viscosity(deck, polymer, machine, model, features)[0],
                     "x_legend": "Polymer viscosity (Pa.s)",
                     "y": data.final_radius_viscosity(deck, polymer, machine, model, features)[1],
                     "y_legend" : "Final fiber radius (m)", "color": "co",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/final_radius_viscosity.pdf",
                     "panda_file_title" : "./data_files/PandaViscosity.csv"})
                     
        organized_data.append({"x": data.radius_x(deck, polymer, machine, model, features)[0],
                     "x_legend": "Axial coordinate x (m)",
                     "y": data.radius_x(deck, polymer, machine, model, features)[1],
                     "y_legend" : "Radius (m)", "color": "ro",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/radius_x.pdf",
                     "panda_file_title" : "./data_files/PandaAxialCoordinate.csv"})

        return organized_data