import itertools
from machine_abstractions.statemachine import StateMachine, State

class TopCardMachine(StateMachine):
    def __init__(self, game, players):
        self.turnStates = [self.Turn(self, p) for p in players]
        super().__init__(game)
        self.StartTC(self, self.turnStates)
        self.playerIndex = 0
        
    def getCurrentState(self):
        return self.currentState
        
    # returns all the states in a flat list
    def getAllStates(self):
        return list(itertools.chain.from_iterable([[self.StartTC], self.turnStates, [self.Win]]))
    
    class StartTC(State):
        def __init__(self, machine, turnStates):
            super().__init__(machine)
            self.currentPlayer = turnStates[0].getPlayer()
            self.machine.setCurrentState(turnStates[0])
            self.machine.game.setCurrentPlayer(self.currentPlayer)
            
    class Turn(State):
        def __init__(self, machine, player):
            super().__init__(machine)
            self.currentPlayer = player
            
        def getPlayer(self):
            return self.currentPlayer
        
        def setNextPlayer(self):
            self.machine.playerIndex += 1
            if self.machine.playerIndex == len(self.machine.turnStates):
                self.machine.playerIndex = 0
            self.machine.game.setCurrentPlayer(self.machine.turnStates[self.machine.playerIndex].getPlayer())
            self.machine.setCurrentState(self.machine.turnStates[self.machine.playerIndex])
            
        def checkWin(self):
            if self.currentPlayer.numCards() == 0:
                self.machine.setCurrentState(self.machine.Win)
                self.machine.game.winner = self.currentPlayer
                
        def check(self, cardsPlayed):
            if self.processCurrent(cardsPlayed):
                return True
            else:
                return False
        
        def processCurrent(self, cardsPlayed):
            return self.machine.game.rules[len(cardsPlayed) - 2]("").canPlay(*cardsPlayed)
            
            
    