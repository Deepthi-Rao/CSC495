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
            for i in range(0, len(self.machine.game.players)):
                if(self.machine.game.players[i].getHand().size() == 52):
                    self.machine.setCurrentState(self.machine.Win(self.machine))
                    self.machine.currentState.processCurrent(self.machine.game.players[i])
                    return True


        def check(self, cardPlayed):

            if self.checkWin():
                return
            if (cardPlayed != None):
                self.currentInfo()
                self.machine.game.pile.push(cardPlayed)
            self.machine.game.incrementTurnIndex()
            if self.processCurrent():
                self.machine.setCurrentState(self.machine.Slappable(self.machine))
                self.machine.game.setCurrentPlayer()
            else:

                self.machine.setCurrentState(self.machine.NonSlappable(self.machine))
                self.machine.game.setCurrentPlayer()

    # this is the non slappable state
    class NonSlappable(State):

        def checkWin(self):
            for i in range(0, len(self.machine.game.players)):
                if(self.machine.game.players[i].getHand().size() == 52):
                    self.machine.setCurrentState(self.machine.Win(self.machine))
                    self.machine.currentState.processCurrent(self.machine.game.players[i])
                    return True

        def check(self, cardPlayed):

            if self.checkWin():
                return
            if(cardPlayed != None):
                self.currentInfo()
                self.machine.game.pile.push(cardPlayed)
            self.machine.game.incrementTurnIndex()
            if self.processCurrent():

                self.machine.setCurrentState(self.machine.Slappable(self.machine))
                self.machine.game.setCurrentPlayer()
            else:

                self.machine.setCurrentState(self.machine.NonSlappable(self.machine))
                self.machine.game.setCurrentPlayer()

    # this is the win state
    class Win(State):
        def processCurrent(self, player):
            print(player.getName() + " has won the game!" )
