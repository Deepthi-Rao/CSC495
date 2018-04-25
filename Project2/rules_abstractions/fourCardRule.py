from rules_abstractions.rule import Rule

#this defines processes for a two card rule
class FourCardRule(Rule):

    def __init__(self, name, machine):
        self.name = name
        self.machine = machine

    # this processes the current play based on 4 cards passed in, including the comp card
    # will be customized when rule is declared
    # returns true or false
    def canPlay2(self, compCard, card1, card2, card3):
        return