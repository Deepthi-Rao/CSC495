from rules_abstractions.threeCardRule import ThreeCardRule
from rules_abstractions.twoCardRule import TwoCardRule
from rules_abstractions.fourCardRule import FourCardRule

#converts face cards to integers for play
def rankToInt(rank):
    ranks = { "A" : 1,
             "J" : 11,
             "Q" : 12,
             "K" : 13
        }
    if isinstance(rank, int):
        return rank
    return ranks[rank]
    
# adds up ranks of all the cards passed in
# takes in multiple card parameters
def getPlayValue(*args):
    total = 0
    for card in args:
        total += rankToInt(card.getRank())
    return total
        
class Play1Rule(TwoCardRule):
    def canPlay(self, compCard, card1):
        if compCard.getRank() == card1.getRank():
            return True
        return False

class Play2Rule(ThreeCardRule):
    def canPlay(self, compCard, card1, card2):
        #special case: compCard is an Ace
        if compCard.getRank() == "A":
            if getPlayValue(card1, card2) == 14:
                return True
            return False
        else:
            if getPlayValue(card1, card2) == rankToInt(compCard.getRank()):
                return True
            return False

class Play3Rule(FourCardRule):
    def canPlay(self, compCard, card1, card2, card3):
        #special case: compCard is an Ace
        if compCard.getRank() == "A":
            if getPlayValue(card1, card2, card3) == 14:
                return True
            return False
        else:
            if getPlayValue(card1, card2, card3) == rankToInt(compCard.getRank()):
                return True
            return False