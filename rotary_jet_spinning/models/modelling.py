#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt


class RJSModel:
# from [mellado_simple_2011] see biblio.bib

    # Initializer Attributes
    def __init__(self, polymer, machine):
        self.omega_th = self.critical_rotational_velocity_threshold(polymer.surface_tension, machine.orifice_radius, machine.reservoir_radius, polymer.density)
        self.init_velocity = self.initial_velocity(self.omega_th, machine.reservoir_radius)
        self.nu = self.kinematic_viscosity(polymer.viscosity, polymer.density)
        self.final_radius(machine.orifice_radius, self.init_velocity, self.nu, machine.collector_radius, machine.angular_velocity)
    

    def critical_rotational_velocity_threshold(self, surface_tension, orifice_radius, s0, rho):
        """RJS
        Prediction of the critical rotational velocity for jet ejection

        :Input:
        - *surface_tension* (float) - surface tension (kg/s^2)
        - *orifice_radius* (float) - radius of the orifice (m)
        - *s0* (float) - radius of the reservoir (m)
        - *rho* (float) - density (kg/m^3)
        
        :Returns:
        (float) - Critical rotational speed for jet ejection (rounds per second)
        
        """
        return sqrt(surface_tension/(orifice_radius**2*s0*rho))
        
    def initial_velocity(self, omega_th, s0):
        """RJS
        Prediction of the initial velocity of the fiber

        :Input:
        - *omega_th* (float) - Critical rotational speed for jet ejection (rounds per second)
        - *s0* (float) - radius of the reservoir (m)
        
        :Returns:
        (float) - Initial axial velocity (m/s)
        
        """
        return omega_th*s0
        
    def sigma(self, surface_tension, x_position, r0, initial_velocity):
        """RJS
        sigma=surface_tension * x_position / (r0 * initial_velocity) * 10**(-3)

        Sigma is used in the next function for the prediction of the fiber radius
        as a function of the axial coordinate
        
        :Input:
        - *surface_tension* (float) - surface tension (kg/s^2)
        - *x_position* (float) - axial coordinate x (m)
        - *r0* (float) - initial radius of the jet = orifice radius a (m)
        - *initial_velocity* (float) - initial axial velocity (m/s)
        
        :Returns:
        (float) - sigma (in kg/(m.s))
        
        """
        return surface_tension*x_position/(r0*initial_velocity)
        
    def radius(self, r0, rho, initial_velocity, x_position, mu, Sigma, omega):
        """RJS
        Prediction of the radius of the jet in steady state as a function of
        the axial coordinate x

        :Input:
        - *r0* (float) - initial radius of the jet = orifice radius a (m)
        - *rho* (float) - density (kg/m^3)
        - *initial_velocity* (float) - initial axial velocity (m/s)
        - *x_position* (float) - axial coordinate x (m)
        - *mu* (float) - viscosity (Pa.s)
        - *Sigma* (float) - call sigma function : sigma(surface_tension, x_position,
                                                    r0, initial_velocity)
        - *omega* (float) - angular velocity (rounds per second)
        
        :Returns:
        (float) - final radius (m)
        
        """
        return r0*sqrt(rho*initial_velocity*x_position/(mu-Sigma+sqrt((mu-Sigma)**2+(rho*omega*x_position**2)**2)))
        
    def final_radius(self, orifice_radius, initial_velocity, nu, Rc, omega):
        """RJS
        Prediction of the final radius

        :Input:
        - *orifice_radius* (float) - initial radius of the jet = orifice radius (m)
        - *initial_velocity* (float) - initial axial velocity (m/s)
        - *nu* (float) - kinematic viscosity (m^2/s) : call kinematic_viscosity function 
                                                       (kinematic_viscosity(mu, rho))
        - *Rc* (float) - radius of the collector (m)
        - *omega* (float) - angular velocity (rounds/s)
        
        :Returns:
        (float) - approximation of the final radius  (m)
        """
        return orifice_radius*sqrt(initial_velocity*nu)/(Rc**(3/2)*omega)
        
    def kinematic_viscosity(self, mu, rho):
        """RJS
        Compute the kinematic viscosity
        
        :Input:
        - *mu* (float) - viscosity (Pa.s)
        - *rho* (float) - density (kg/m^3)
        
        :Returns:
        (float) - kinematic viscosity (m^2/s)
        """
        return mu/rho

