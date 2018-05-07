
#This is the rules_abstractions Abstraction class, to help implement custom rules_abstractions that will be defined within
# the specific rules_abstractions classes for each game.

class Rule:

    def __init__(self, name):
        self.name = name;
    #returns true if the move is valid
    def canPlay(self):
        return

    # converts face cards to integers for play
    def rankToInt(self, rank):
        ranks = {"A": 1,
                 "J": 11,
                 "Q": 12,
                 "K": 13
                 }
        if isinstance(rank, int):
            return rank
        return ranks[rank]

    # adds up ranks of all the cards passed in
    # takes in multiple card parameters
    def getPlayValue(self, *args):
        total = 0
        for card in args:
            total += self.rankToInt(card.getRank)
        return total
