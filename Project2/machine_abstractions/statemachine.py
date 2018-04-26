from rules_abstractions.threeCardRule import ThreeCardRule
from rules_abstractions.fourCardRule import FourCardRule
from rules_abstractions.twoCardRule import TwoCardRule
from machine_abstractions.state import Start, Win

# This is the abstraction for the state machine that will be in each game

class StateMachine:

    #initializes the state machine with a name, the game being passed in and the deck
    def __init__(self, name, game, players, rules, deck):
        self.name = name
        self.game = game
        self.players = players
        self.rules = rules
        self.deck = deck #with stack abstraction properties
        self.pile = None
        #current player default always set to first player in array
        self.currentPlayer = players[0]
        self.currentState = Start()


    # TODO: make a start state
    # make an end state and make getters and setters.

    def run(self):
        pass
            
class SlapMachine(StateMachine):
    def __init__(self, name, game, players, rules, deck):
        super(name, game, players, rules, deck)
        self.pile = None
        self.currentPlayer = players[0]
        self.currentState = Start()