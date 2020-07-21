#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:00:12 2020

@author: amelielaurens
"""

from models_RJS import *

# Predict the minimum angular speed for fiber formation
rho = float(input("Enter the density of the polymer in kg/m^3 : "))
Rc = float(input("Enter the radius of the collector in m : "))
surface_tension = float(input("Enter the surface tension in kg/s^2 : "))
mu = float(input("Enter the viscosity of the polymer in Pa.s : "))
orifice_radius = float(input("Enter the radius of the orifice in m : "))

critical_rotational_velocity = critical_rotational_velocity(rho, Rc, surface_tension, mu, orifice_radius)
print('The minimum angular speed for fiber formation is : %s (in round per second).' %(critical_rotational_velocity))
