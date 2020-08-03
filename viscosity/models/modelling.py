#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Reference : 
Mark G. Dodin Ph.D. (1986) 
Mathematical Models of Polymer Melt Viscosity in Shearing Flow.
Polystyrene and Polypropylene Melts—2
International Journal of Polymeric Materials and Polymeric Biomaterials
1:3, 185-203,
DOI: 10.1080/00914038608078660
"""

from math import *


class Model:

    # Initializer Attributes
    def __init__(self, deck, polymer):
        self.deck = deck
        self.polymer = polymer

    def viscosity(self, B, E, R, T, b, shear_stress_power):
        """ 
        valid for all polymers
        
        :Input:  
        - *B, b* : constant of the material
        - *E* : activation energy of viscous-elastic flow under condition of shear stress = constant
        - *shear_stress_power* : shear stresse to the power of 1/2
        - *R* : gas constant in J/(mol.K)
        - *T* : temperature of experiment (K)
        
        :Returns:
        Melt viscosity in shearing flow

        """
        return B*exp(E/(R*T)-b*shear_stress_power)
