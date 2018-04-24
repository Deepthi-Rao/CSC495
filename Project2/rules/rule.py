#This is the rules Abstraction class, to help implement custom rules that will be defined within
# the specific rules classes for each game.

class Rule:
    def __init__(self):
        self.card1 = None
        self.card2 = None
        self.card3 = None

    # this processes the current play based on 4 cards passed in, including the comp card
    # will be customized when rule is declared
    # returns true or false
    def canPlay2(self, compCard, card1, card2, card3):
        return

    # this processes the current play based on 3 cards passed in, including the comp card
    # will be customized when rule is declared
    # returns true or false
    def canPlay3(self, compCard, card1, card2):
        return

    # this processes the current play based on 2 cards passed in, including the comp card
    # will be customized when rule is declared
    # returns true or false
    def canPlay2(self, compCard, card1):
        return
