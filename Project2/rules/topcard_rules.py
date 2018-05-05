from rules_abstractions.threeCardRule import ThreeCardRule
from rules_abstractions.twoCardRule import TwoCardRule
from rules_abstractions.fourCardRule import FourCardRule

class TopCardRules:

    def __init__(self):
        self.rules = self.getAllRules()



    class Play1Rule(TwoCardRule):
        def canPlay(self, compCard, card1):
            if compCard.getRank == card1.getRank:
                return True
            return False

    class Play2Rule(ThreeCardRule):
        def canPlay(self, compCard, card1, card2):
            #special case: compCard is an Ace
            if compCard.getRank == "A":
                if self.getPlayValue(card1, card2) == 14:
                    return True
                return False
            else:
                if self.getPlayValue(card1, card2) == self.rankToInt(compCard.getRank):
                    return True
                return False

    class Play3Rule(FourCardRule):


        def canPlay(self, compCard, card1, card2, card3):

            #special case: compCard is an Ace
            if compCard.getRank == "A":
                if self.getPlayValue(card1, card2, card3) == 14:
                    return True
                return False
            else:
                if self.getPlayValue(card1, card2, card3) == self.rankToInt(compCard.getRank):
                    return True
                return False

    def getAllRules(self):
        return [self.Play1Rule, self.Play2Rule, self.Play3Rule]