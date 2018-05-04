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
    def __init__(self, machine, cardPlayed = None):
        self.machine = machine
        self.cardPlayed = cardPlayed
        self.rules = self.machine.rules
        self.turnIndex = self.machine.turnIndex
        self.players = self.machine.players
        self.currentPlayer = self.players[self.turnIndex % len(self.players)]
        self.deck = self.machine.deck


    # this displays the current information
    def currentInfo(self):
        self.machine.setCurrentPlayer(self.turnIndex)
        print(self.machine.currentPlayer.getName() + " is playing a Card")

        print(
            self.machine.currentPlayer.getName.getId() + " has played a Card with the properties: Suit " +
                self.cardPlayed.getSuit() + " and Rank "
                + str(self.cardPlayed.getRank()))

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

        canPlay = False

        if(self.cardPlayed == None):
            print("No card played cannot process yet")
            #dont do anything
            return

        for i in range(0, self.rules.size()):
            if self.deck.size() >= 4 and isinstance(self.rules[i], FourCardRule): # if four cards are passed in and is a four card rule
                if(self.rules[i].canPlay(self.cardPlayed, self.deck[0], self.deck[1], self.deck[2]) == True):
                    print("Valid")
                    canPlay = True
                    break

            if self.deck.size() >= 3 and isinstance(self.rules[i], ThreeCardRule): # if three cards are passed in and is a three card rule
                if (self.rules[i].canPlay(self.cardPlayed, self.deck[0], self.deck[1]) == True):
                    print("Valid")
                    canPlay = True
                    break

            if self.deck.size() >= 2 and isinstance(self.rules[i], TwoCardRule): # if two cards are passed in and is a two card rule
                if (self.rules[i].canPlay(self.cardPlayed, self.deck[0]) == True):
                    print("Valid")
                    canPlay = True
                    break
            
            if self.deck.size() >= 1 and isinstance(self.rules[i], OneCardRule): # if one card is passed in and is a one card rule
                if (self.rules[i].canPlay(self.cardPlayed) == True):
                    print("Valid")
                    canPlay = True
                    break

        #once all rules are checked and if nothing returns true then canPlay stays False
        if(canPlay == False):
            # print("Invalid Move")
            pass

    
