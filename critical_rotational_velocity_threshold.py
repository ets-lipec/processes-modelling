#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:50:50 2020

@author: amelielaurens
"""

# Predict the critical rotational velocity for jet ejection

from models_RJS import *

#Choose one machine and one polymer

#Machines
#Super Floss Maxx
#s0 = 0.06985
#orifice_radius = 0.001512

#CANDY-V001
s0 = 0.0635
orifice_radius = 0.000267

#Polymers
#PP
#surface_tension = 0.0436
#rho = 900.

#PLA
surface_tension = 0.0248
rho = 1250.


#If we want the user to enter its own values
#surface_tension = float(input("Enter the surface tension in kg/s^2 : "))
#orifice_radius = float(input("Enter the radius of the orifice in m : "))
#s0 = float(input("Enter the radius of the reservoir in m : "))
#rho = float(input("Enter the density of the polymer in kg/m^3 : "))


critical_rotational_velocity = critical_rotational_velocity_threshold(surface_tension, orifice_radius, s0, rho)
print('The critical rotational velocity threshold for jet ejection is : %s (in round per second).' %(critical_rotational_velocity))
