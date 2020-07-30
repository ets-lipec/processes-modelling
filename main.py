from rotary_jet_spinning import *


cwd = os.getcwd()

deck = Deck(cwd + "/" + "deck.yaml")

machine = RJSMachine(deck)

polymer = Polymer(deck)

model = RJSModel(polymer, machine)

graph = Graph(deck, polymer, machine, model)