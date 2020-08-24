#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rotary_jet_spinning import *


cwd = os.getcwd()
#c=current w=working d=directory

os.makedirs("graphics", exist_ok=True)

os.makedirs("data_files", exist_ok=True)

deck = Deck(cwd + "/" + "deck.yaml")

polymer = Polymer(deck)

machine = RJSMachine(deck)

features = GraphFeatures(deck)

model = RJSModel(polymer, machine)

data = Data(deck, polymer, machine, model, features)

organization = Organization(data, deck, machine, polymer, model, features)

organized_data = organization.organize_data(data, deck, machine, polymer, model, features)

graph = PointGraph(organized_data)

experimental = Experimental(deck)

comparison = Comparison(deck, polymer, machine, model, features, experimental)
