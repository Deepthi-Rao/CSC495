from rules_abstractions.threeCardRule import ThreeCardRule
from rules_abstractions.fourCardRule import FourCardRule
from rules_abstractions.twoCardRule import TwoCardRule
from rules_abstractions.oneCardRule import OneCardRule


#this represents one state
# name is the name of the state
# machine is the machine that the state is contained within
# rules is the array of rules_abstractions that will be passed into each state to process the current card
# the machine will have access to the deck of cards and players etc.

class State:

    # this initializes the state with the rules_abstractions being passed in
    def __init__(self, machine):
        self.machine = machine

    # this displays the current information
    def currentInfo(self):
        print(self.machine.game.currentPlayer.getName() + " has played a Card with the properties: Suit " +
              self.machine.game.cardPlayed.getSuit() + " and Rank " + str(self.machine.game.cardPlayed.getRank))


    #this checks for a valid play
    def check(self):
        return

    #this checks for a win
    def checkWin(self):
        return

    # this processes the current state
    # rules_abstractions is the array of rules_abstractions
    # cards is the array of cards
    def processCurrent(self):

        if(self.machine.game.cardPlayed == None):
            print("No card played by " + self.machine.game.currentPlayer.getName())
            return

        for i in range(0, len(self.machine.game.rules)):

            if self.machine.game.pile.size() >= 4 and isinstance(self.machine.game.rules[i], FourCardRule): # if four cards are passed in and is a four card rule
                if(self.machine.game.rules[i].canPlay(self.machine.game.cardPlayed, self.machine.game.pile.peekSecond(),
                                                      self.machine.game.pile.peekThird(), self.machine.game.pile.peekFourth()) == True):
                    self.machine.game.displayMessage = self.machine.game.rules[i].name + " Employed."

                    return True

            if self.machine.game.pile.size() >= 3 and isinstance(self.machine.game.rules[i], ThreeCardRule): # if three cards are passed in and is a three card rule
                if (self.machine.game.rules[i].canPlay(self.machine.game.cardPlayed,
                                                       self.machine.game.pile.peekSecond(), self.machine.game.pile.peekThird()) == True):
                    self.machine.game.displayMessage = self.machine.game.rules[i].name + " Employed."
                    return True

            if self.machine.game.pile.size() >= 2 and isinstance(self.machine.game.rules[i], TwoCardRule): # if two cards are passed in and is a two card rule
                if (self.machine.game.rules[i].canPlay(self.machine.game.cardPlayed, self.machine.game.pile.peekSecond()) == True):
                    self.machine.game.displayMessage = self.machine.game.rules[i].name + " Employed."
                    return True

            
            if self.machine.game.pile.size() >= 1 and isinstance(self.machine.game.rules[i], OneCardRule): # if one card is passed in and is a one card rule
                if (self.machine.game.rules[i].canPlay(self.machine.game.cardPlayed) == True):
                    self.machine.game.displayMessage = self.machine.game.rules[i].name + " Employed."
                    return True

        return False




    
