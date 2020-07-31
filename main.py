from rotary_jet_spinning import *


cwd = os.getcwd()

deck = Deck(cwd + "/" + "deck.yaml")

machine = RJSMachine(deck)

polymer = Polymer(deck)

model = RJSModel(polymer, machine)

data = Data(deck, polymer, machine, model)

organization = Organization(data, deck, machine, polymer, model)

organized_data = organization.organize_data(data, deck, machine, polymer, model)

graph = PointGraph(organized_data)
