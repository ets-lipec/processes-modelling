<<<<<<< HEAD
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

>>>>>>> f3c4f03a977059ca4f013ba64f45c1bd2a586c9c
from rotary_jet_spinning import *


cwd = os.getcwd()

deck = Deck(cwd + "/" + "deck.yaml")

machine = RJSMachine(deck)

polymer = Polymer(deck)

<<<<<<< HEAD
model = RJSModel(polymer, machine)

data = Data(deck, polymer, machine, model)

organization = Organization(data, deck, machine, polymer, model)

organized_data = organization.organize_data(data, deck, machine, polymer, model)

graph = PointGraph(organized_data)
=======
features = GraphFeatures(deck)

model = RJSModel(polymer, machine)

data = Data(deck, polymer, machine, model, features)

organization = Organization(data, deck, machine, polymer, model, features)

organized_data = organization.organize_data(data, deck, machine, polymer, model, features)

graph = PointGraph(organized_data)

# comparison = Comparison(deck, polymer, machine, model)
>>>>>>> f3c4f03a977059ca4f013ba64f45c1bd2a586c9c
