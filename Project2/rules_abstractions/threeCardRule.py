from rules_abstractions.rule import Rule

#This will process any rules_abstractions with 3 cards including the current card
class ThreeCardRule(Rule):

    #this initializes the class with the name and the machine
    def __init__(self, name, machine):
        self.name = name
        self.machine = machine


    # this processes the current play based on 3 cards passed in, including the comp card
    # will be customized when rule is declared
    # returns true or false
    def canPlay(self, compCard, card1, card2):
        return

