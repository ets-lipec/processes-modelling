from viscosity import *

cwd = os.getcwd()

deck = Deck(cwd + "/" + "viscosity.yaml")

polymer = Polymer(deck)

model = Model(deck, polymer)

graph = Graph(deck, polymer, model)
