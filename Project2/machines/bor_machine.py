import itertools
from machine_abstractions.statemachine import StateMachine, State

class BoRMachine(StateMachine):
    
    def __init__(self, game, players):
        self.turnStates = [self.Turn(p) for p in players]
        super(game)
        
    
    # returns all the states in a flat list
    def getAllStates(self):
        return list(itertools.chain.from_iterable([self.Start, self.turnStates, self.Win]))
    
    class Start(State):
        def check(self, turnStates):
            self.currentIndex = 0
            self.currentPlayer = turnStates[0].getPlayer()
            self.machine.setCurrentState(turnStates[0])
            
    class Turn(State):
        def __init__(self, player):
            self.currentPlayer = player
            
        def getPlayer(self):
            return self.currentPlayer
        
        def check(self, cardPlayed, guess):
            self.machine.game.pile.push(cardPlayed)
            if self.processCurrent(guess):
                pass
            
        def processCurrent(self, guess):
            return self.machine.game.rules[0].canPlay(self.machine.game.cardPlayed, guess)
                
        