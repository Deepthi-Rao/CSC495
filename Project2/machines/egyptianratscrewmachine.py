from machine_abstractions.statemachine import StateMachine
from machine_abstractions.statemachine import State

class SlapMachine(StateMachine):
    def __init__(self, name, game, players, rules, deck):
        super(name, game, players, rules, deck)
        self.pile = None
        self.currentPlayer = players[0]
        self.currentState = self.Start()