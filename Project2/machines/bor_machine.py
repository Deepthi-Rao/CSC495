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
            self.playerIndex = 0
            self.currentPlayer = turnStates[0].getPlayer()
            self.machine.setCurrentState(turnStates[0])
            self.machine.game.setCurrentPlayer(self.currentPlayer)
            
    class Turn(State):
        def __init__(self, player):
            self.currentPlayer = player
            self.numGuesses = 0
            
        def getPlayer(self):
            return self.currentPlayer
        
        def check(self, cardPlayed, guess):
            self.machine.game.pile.push(cardPlayed)
            if self.processCurrent(guess):
                if self.numGuesses >= 3:
                    self.playerIndex += 1
                    self.machine.setCurrentState(self.turnStates[self.playerIndex])
                else:
                    self.numGuesses += 1
            else:
                self.machine.game.getCurrentPlayer().scorePoints(self.numGuesses+1)
                self.playerIndex += 1
                self.machine.game.setCurrentPlayer(self.turnStates[self.playerIndex].getPlayer())
                self.machine.setCurrentState(self.turnStates[self.playerIndex])
            
        def processCurrent(self, guess):
            return self.machine.game.rules[0].canPlay(self.machine.game.cardPlayed, guess)
                
        