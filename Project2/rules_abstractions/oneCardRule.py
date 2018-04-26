from rules_abstractions.rule import Rule

#This will process any rules_abstractions with 2 cards including the current card
class OneCardRule(Rule):

    #this initializes the class with the name and the machine
    def __init__(self, name, machine):
        self.name = name
        self.machine = machine


    # this processes the current play based on 2 cards passed in, including the comp card
    # will be customized when rule is declared
    # returns true or false
    def canPlay(self, compCard):
        return
