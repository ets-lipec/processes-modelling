<<<<<<< HEAD
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>>>>>> f3c4f03a977059ca4f013ba64f45c1bd2a586c9c


class Organization:

<<<<<<< HEAD
    def __init__(self, data, deck, machine, polymer, model):
=======
    def __init__(self, data, deck, machine, polymer, model, features):
>>>>>>> f3c4f03a977059ca4f013ba64f45c1bd2a586c9c
        self.data = data
        self.deck = deck
        self.machine = machine
        self.polymer = polymer
        self.model = model
<<<<<<< HEAD
        self.organize_data(data, deck, machine, polymer, model)
    

    def organize_data(self, data, deck, machine, polymer, model):
        
        organized_data = [{"x": data.final_radius_orifice_radius(deck, polymer, machine, model)[0],
                "x_legend": "Radius of the orifice (m)",
                "y": data.final_radius_orifice_radius(deck, polymer, machine, model)[1],
=======
        self.organize_data(data, deck, machine, polymer, model, features)
    

    def organize_data(self, data, deck, machine, polymer, model, features):
        
        organized_data = [{"x": data.final_radius_orifice_radius(deck, polymer, machine, model, features)[0],
                "x_legend": "Radius of the orifice (m)",
                "y": data.final_radius_orifice_radius(deck, polymer, machine, model, features)[1],
>>>>>>> f3c4f03a977059ca4f013ba64f45c1bd2a586c9c
                "y_legend" : "Final radius (m)", "color": "ro",
                "title": " %s / %s " % (machine.name, polymer.name),
                "save_as": "./graphics/final_radius_orifice_radius.pdf"}] 
                
<<<<<<< HEAD
        organized_data.append({"x": data.final_radius_omega(deck, polymer, machine, model)[0],
                     "x_legend": "Angular velocity (rounds per second)",
                     "y": data.final_radius_omega(deck, polymer, machine, model)[1],
                     "y_legend" : "Final radius (m)", "color": "bo",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/final_radius_omega.pdf"})
                     
        organized_data.append({"x": data.final_radius_collector_radius(deck, polymer, machine, model)[0],
                     "x_legend": "Collector distance (m)",
                     "y": data.final_radius_collector_radius(deck, polymer, machine, model)[1],
=======
        organized_data.append({"x": data.final_radius_angular_velocity(deck, polymer, machine, model, features)[0],
                     "x_legend": "Angular velocity (rounds per second)",
                     "y": data.final_radius_angular_velocity(deck, polymer, machine, model, features)[1],
                     "y_legend" : "Final radius (m)", "color": "bo",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/final_radius_angular_velocity.pdf"})
                     
        organized_data.append({"x": data.final_radius_collector_radius(deck, polymer, machine, model, features)[0],
                     "x_legend": "Collector distance (m)",
                     "y": data.final_radius_collector_radius(deck, polymer, machine, model, features)[1],
>>>>>>> f3c4f03a977059ca4f013ba64f45c1bd2a586c9c
                     "y_legend" : "Final radius (m)", "color": "go",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/final_radius_collector_radius.pdf"})
                     
<<<<<<< HEAD
        organized_data.append({"x": data.final_radius_reservoir_radius(deck, polymer, machine, model)[0],
                     "x_legend": "Radius of the reservoir (m)",
                     "y": data.final_radius_reservoir_radius(deck, polymer, machine, model)[1],
=======
        organized_data.append({"x": data.final_radius_reservoir_radius(deck, polymer, machine, model, features)[0],
                     "x_legend": "Radius of the reservoir (m)",
                     "y": data.final_radius_reservoir_radius(deck, polymer, machine, model, features)[1],
>>>>>>> f3c4f03a977059ca4f013ba64f45c1bd2a586c9c
                     "y_legend" : "Final radius (m)", "color": "yo",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/final_radius_reservoir_radius.pdf"})
                     
<<<<<<< HEAD
        organized_data.append({"x": data.final_radius_density(deck, polymer, machine, model)[0],
                     "x_legend": "Density (kg/m^3)",
                     "y": data.final_radius_density(deck, polymer, machine, model)[1],
=======
        organized_data.append({"x": data.final_radius_density(deck, polymer, machine, model, features)[0],
                     "x_legend": "Density (kg/m^3)",
                     "y": data.final_radius_density(deck, polymer, machine, model, features)[1],
>>>>>>> f3c4f03a977059ca4f013ba64f45c1bd2a586c9c
                     "y_legend" : "Final radius (m)", "color": "ko",
                     "title": " %s / %s " % (machine.name, polymer.name),
                    "save_as": "./graphics/final_radius_density.pdf"})
                    
<<<<<<< HEAD
        organized_data.append({"x": data.final_radius_surface_tension(deck, polymer, machine, model)[0],
                     "x_legend": "Surface tension (kg/s^2)",
                     "y": data.final_radius_surface_tension(deck, polymer, machine, model)[1],
=======
        organized_data.append({"x": data.final_radius_surface_tension(deck, polymer, machine, model, features)[0],
                     "x_legend": "Surface tension (kg/s^2)",
                     "y": data.final_radius_surface_tension(deck, polymer, machine, model, features)[1],
>>>>>>> f3c4f03a977059ca4f013ba64f45c1bd2a586c9c
                     "y_legend" : "Final radius (m)", "color": "mo",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/final_radius_surface_tension.pdf"})
                     
<<<<<<< HEAD
        organized_data.append({"x": data.final_radius_viscosity(deck, polymer, machine, model)[0],
                     "x_legend": "Polymer viscosity (Pa.s)",
                     "y": data.final_radius_viscosity(deck, polymer, machine, model)[1],
=======
        organized_data.append({"x": data.final_radius_viscosity(deck, polymer, machine, model, features)[0],
                     "x_legend": "Polymer viscosity (Pa.s)",
                     "y": data.final_radius_viscosity(deck, polymer, machine, model, features)[1],
>>>>>>> f3c4f03a977059ca4f013ba64f45c1bd2a586c9c
                     "y_legend" : "Final radius (m)", "color": "co",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/final_radius_viscosity.pdf"})
                     
<<<<<<< HEAD
        organized_data.append({"x": data.radius_x(deck, polymer, machine, model)[0],
                     "x_legend": "Axial coordinate x (m)",
                     "y": data.radius_x(deck, polymer, machine, model)[1],
=======
        organized_data.append({"x": data.radius_x(deck, polymer, machine, model, features)[0],
                     "x_legend": "Axial coordinate x (m)",
                     "y": data.radius_x(deck, polymer, machine, model, features)[1],
>>>>>>> f3c4f03a977059ca4f013ba64f45c1bd2a586c9c
                     "y_legend" : "Radius (m)", "color": "ro",
                     "title": " %s / %s " % (machine.name, polymer.name),
                     "save_as": "./graphics/radius_x.pdf"})

<<<<<<< HEAD
        return organized_data
=======
        return organized_data
>>>>>>> f3c4f03a977059ca4f013ba64f45c1bd2a586c9c
