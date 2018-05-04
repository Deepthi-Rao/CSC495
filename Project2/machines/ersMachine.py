from machine_abstractions.statemachine import StateMachine
from machine_abstractions.statemachine import State

class ERSMachine(StateMachine):


    #returns all the states for ERS
    def getAllStates(self):
        return [self.Start, self.Slappable, self.NonSlappable, self.Win]

    # this is the start state
    class Start(State):

        def begin(self):
            self.currentInfo()
            self.machine.turnIndex = self.machine.turnIndex + 1
            if self.processCurrent():
                self.machine.setCurrentState(self.machine.Slappable(self.machine, self.cardPlayed))
            else:
                self.machine.setCurrentState(self.machine.NonSlappable(self.machine, self.cardPlayed))


    #this is the is slappable state
    class Slappable(State):
        def checkWin(self):
            for i in range(0, self.players.length()):
                if(self.players[i].getCardsInHand().size() == 52):
                    self.machine.setCurrentState(self.machine.Win(self.machine))
                    self.machine.currentState.processCurrent()

        def check(self, cardPlayed):
            self.currentInfo()
            self.machine.turnIndex = self.machine.turnIndex + 1
            if self.processCurrent():
                self.machine.setCurrentState(self.machine.Slappable(self.machine, cardPlayed))
            else:
                self.machine.setCurrentState(self.machine.NonSlappable(self.machine, cardPlayed))

    #this is the non slappable state
    class NonSlappable(State):

        def checkWin(self):
            for i in range(0, self.players.length()):
                if(self.players[i].getCardsInHand().size() == 52):
                    self.machine.setCurrentState(self.machine.Win(self.machine))
                    self.machine.currentState.processCurrent()

        def check(self, cardPlayed):
            self.currentInfo()
            self.machine.turnIndex = self.machine.turnIndex + 1
            if self.processCurrent():
                self.machine.setCurrentState(self.machine.Slappable(self.machine, cardPlayed))
            else:
                self.machine.setCurrentState(self.machine.NonSlappable(self.machine, cardPlayed))

    #this is the win state
    class Win(State):

        def processCurrent(self):
            print(self.machine.currentPlayer.getName() + 'has won the game!!!!')












