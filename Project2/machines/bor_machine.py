import itertools
from machine_abstractions.statemachine import StateMachine, State

class BoRMachine(StateMachine):
    
    def __init__(self, game, players):
        self.turnStates = [self.Turn(self, p) for p in players]
        super().__init__(game)
        self.StartBoR(self, self.turnStates)
        self.playerIndex = 0
        
    def getCurrentState(self):
        return self.currentState
        
    
    # returns all the states in a flat list
    def getAllStates(self):
        return list(itertools.chain.from_iterable([[self.Start], self.turnStates, [self.Win]]))
    
    class StartBoR(State):
        def __init__(self, machine, turnStates):
            super().__init__(machine)
            self.currentPlayer = turnStates[0].getPlayer()
            self.machine.setCurrentState(turnStates[0])
            self.machine.game.setCurrentPlayer(self.currentPlayer)
            
    class Turn(State):
        def __init__(self, machine, player):
            super().__init__(machine)
            self.currentPlayer = player
            self.numGuesses = 0
            
        def getPlayer(self):
            return self.currentPlayer
        
        def setNextPlayer(self):
            self.machine.playerIndex += 1
            if self.machine.playerIndex == len(self.machine.turnStates):
                self.machine.playerIndex = 0
            self.machine.game.setCurrentPlayer(self.machine.turnStates[self.machine.playerIndex].getPlayer())
            self.machine.setCurrentState(self.machine.turnStates[self.machine.playerIndex])
                
        
        def check(self, cardPlayed, guess):
            self.machine.game.pile.push(cardPlayed)
            if self.processCurrent(guess):
                print("You have guessed correctly!\n")
                self.numGuesses += 1
                if self.numGuesses >= 3:
                    self.numGuesses = 0
                    print("You have guessed correctly three times.")
                    print("Your turn has ended.\n")
                    self.setNextPlayer()
                else:
                    print("You have guessed correctly " + str(self.numGuesses) + " time(s).\n")
            else:
                print("Your guess is incorrect.")
                self.machine.game.getCurrentPlayer().scorePoints(self.numGuesses+1)
                print("You now have " + str(self.machine.game.getCurrentPlayer().getPoints()) + " points.")
                print("Your turn has ended.\n")
                self.numGuesses = 0
                self.setNextPlayer()
                
            
        def processCurrent(self, guess):
            m = self.machine
            g = m.game
            rule =  g.rules[0]
            card = g.cardPlayed
            r = rule.canPlay(rule, card, guess)
            return r
        
        