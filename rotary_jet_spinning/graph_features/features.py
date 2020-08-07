#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class GraphFeatures:

    # Initializer Attributes
    def __init__(self, deck):
        self.discretisation = int(deck.doc['Graphic features']['Discretisation'])
        # The higher the discretisation number is, the finer the discretisation will be,
        # there will be more points on the graphic