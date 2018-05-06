from rules_abstractions.threeCardRule import ThreeCardRule
from rules_abstractions.fourCardRule import FourCardRule
from rules_abstractions.twoCardRule import TwoCardRule
from machine_abstractions.state import State

# This is the abstraction for the state machine that will be in each game

class StateMachine:

    #initializes the state machine with a name, the game being passed in and the deck
    def __init__(self, game):
        self.game = game
        self.game.setCurrentPlayer()
        self.currentState = self.Start(self)
        self.states = self.getAllStates()

    # set the current state
    def setCurrentState(self, state):
        self.currentState = state

    #return all the states created
    def getAllStates(self):
        return

    # this is the start state
    class Start(State):
        #starts the game
        def begin(self):
            return
        
    class Turn(State):
        def __init__(self, player):
            self.currentPlayer = player
            
        def getPlayer(self):
            return self.currentPlayer

    # this is the win state
    class Win(State):
        """The game has been won"""
        def isWon(self):
            return True;


