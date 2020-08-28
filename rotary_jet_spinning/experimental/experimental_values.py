#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Experimental:

    # Initializer Attributes
    def __init__(self, deck):
        self.angular_velocities_exp = list(deck.doc['Experimental Datas']['Angular Velocities'])
        self.final_radius_exp = list(deck.doc['Experimental Datas']['Final Radius'])