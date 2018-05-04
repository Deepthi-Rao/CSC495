from rules_abstractions.threeCardRule import ThreeCardRule
from rules_abstractions.fourCardRule import FourCardRule
from rules_abstractions.twoCardRule import TwoCardRule
from machine_abstractions.state import State

# This is the abstraction for the state machine that will be in each game

class StateMachine:

    #initializes the state machine with a name, the game being passed in and the deck
    def __init__(self, game, players, rules, deck):
        self.game = game
        self.players = players
        self.rules = rules
        self.deck = deck #with stack abstraction properties
        self.pile = None
        #current player default always set to first player in array
        self.turnIndex = 0;
        self.currentState = self.Start(self)
        self.currentPlayer = players[0]
        self.states = self.getAllStates()

    # set the current player
    def setCurrentPlayer(self, turnIndex):
        self.currentPlayer = self.players[turnIndex % self.players.length()]

    # set the current state
    def setCurrentState(self, state):
        self.setCurrentState()

    #return all the states created
    def getAllStates(self):
        return

    class Start:
        #starts the game
        def begin(self):
            return

    class Win(State):
        """The game has been won"""
        def isWon(self):
            return True;


