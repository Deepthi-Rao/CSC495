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
    def __init__(self, name, machine, rules):
        self.name = name
        self.machine = machine
        self.rules = rules
        
    # will be overridden in Win state
    def isWon(self):
        return False

    # this processes the current state
    # rules_abstractions is the array of rules_abstractions
    # cards is the array of cards
    def processCurrent(self, cardPlayed, cards):
        rules = self.rules
        canPlay = False
        for i in range(0, rules.size()):
            if cards.size() == 4 and isinstance(rules[i], FourCardRule): # if four cards are passed in and is a four card rule
                if(rules[i].canPlay(cardPlayed, cards[0], cards[1], cards[2]) == True):
                    print("Valid Move")
                    canPlay = True
                    break

            elif (cards.size() == 3 and isinstance(rules[i], ThreeCardRule)): # if three cards are passed in and is a three card rule
                if (rules[i].canPlay(cardPlayed, cards[0], cards[1]) == True):
                    print("Valid Move")
                    canPlay = True
                    break

            elif (cards.size() == 2 and isinstance(rules[i], TwoCardRule)): # if two cards are passed in and is a two card rule
                if (rules[i].canPlay(cardPlayed, cards[0]) == True):
                    print("Valid Move")
                    canPlay = True
                    break
            
            elif (cards.size() == 1 and isinstance(rules[i], OneCardRule)): # if one card is passed in and is a one card rule
                if (rules[i].canPlay(cardPlayed) == True):
                    print("Valid Move")
                    canPlay = True
                    break

        #once all rules are checked and if nothing returns true then canPlay stays False
        if(canPlay == False):
            # print("Invalid Move")
            pass

        #TODO: penalize player, set next player, call transition method to set next value

        self.transition()


    #custom to state will set next method for state machine
    def transition(self):
        return self
    
