from machine_abstractions.statemachine import StateMachine
from machine_abstractions.statemachine import State

class ERSMachine(StateMachine):

    #returns all the states for ERS
    def getAllStates(self):
        return [self.Start, self.Slappable, self.NonSlappable, self.Win]

    # this is the start state
    class Start(State):

        def check(self, cardPlayed):
            self.currentInfo()
            self.machine.game.pile.push(cardPlayed)
            self.machine.game.incrementTurnIndex()
            if self.processCurrent():
                self.machine.setCurrentState(self.machine.Slappable(self.machine))
                self.machine.game.setCurrentPlayer()
            else:
                self.machine.setCurrentState(self.machine.NonSlappable(self.machine))
                self.machine.game.setCurrentPlayer()


    # this is the is slappable state
    class Slappable(State):
        def checkWin(self):
            for i in range(0, self.machine.game.players.length()):
                if(self.machine.game.players[i].getCardsInHand().size() == 52):
                    self.machine.setCurrentState(self.machine.Win(self.machine))
                    self.machine.currentState.processCurrent()

        def check(self, cardPlayed):
            self.currentInfo()
            self.machine.game.pile.push(cardPlayed)
            self.machine.game.incrementTurnIndex()
            if self.processCurrent():
                print("slap")
                self.machine.setCurrentState(self.machine.Slappable(self.machine))
                self.machine.game.setCurrentPlayer()
            else:
                print(" non slap")
                self.machine.setCurrentState(self.machine.NonSlappable(self.machine))
                self.machine.game.setCurrentPlayer()

    # this is the non slappable state
    class NonSlappable(State):

        def checkWin(self):
            for i in range(0, self.machine.players.length()):
                if(self.machine.players[i].getCardsInHand().size() == 52):
                    self.machine.setCurrentState(self.machine.Win(self.machine))
                    self.machine.currentState.processCurrent()

        def check(self, cardPlayed):
            self.currentInfo()
            self.machine.game.pile.push(cardPlayed)
            self.machine.game.incrementTurnIndex()
            if self.processCurrent():
                print("slap")
                self.machine.setCurrentState(self.machine.Slappable(self.machine))
                self.machine.game.setCurrentPlayer()
            else:
                print("non Slap")
                self.machine.setCurrentState(self.machine.NonSlappable(self.machine))
                self.machine.game.setCurrentPlayer()

    # this is the win state
    class Win(State):

        def processCurrent(self):
            print(self.machine.currentPlayer.getName() + 'has won the game!!!!')
