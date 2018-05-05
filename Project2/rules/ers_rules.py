from rules_abstractions.oneCardRule import OneCardRule
from machines.ersMachine import ERSMachine
from rules_abstractions.twoCardRule import TwoCardRule
from rules_abstractions.threeCardRule import ThreeCardRule

# in ERS, "valid" cards depend on the machine that's used
# playing a face card would be a "valid" play in the turn machine, and the player
# would pick up the pile
# in the slap machine, only a card fitting the slap rules would return true
class ERSRules:

    class FaceRule(OneCardRule):
        def canPlay(self, compCard):
            if compCard.isFaceCard():

                return True
            return False

    class DoubleRule(TwoCardRule):
        def canPlay(self, compCard, card1):
            if compCard.getRank == card1.getRank:
                return True
            return False

    class SandwichRule(ThreeCardRule):
        def canPlay(self, compCard, card1, card2):
            if compCard.getRank == card2.getRank:

                return True
            return False

    class TensRule(TwoCardRule):
        def canPlay(self, compCard, card1):
            try:
                if (compCard.getRank + card1.getRank) == 10:
                    return True
            # if rank is not an integer
            except TypeError:
                pass
            return False

    class MarriageRule(TwoCardRule):
        def canPlay(self, compCard, card1):
            if compCard.getRank == "K" and card1.getRank == "Q":
                return True
            elif compCard.getRank == "Q" and card1.getRank == "K":
                return True
            return False

    def getAllRules(self):
        return [self.FaceRule(), self.DoubleRule(), self.SandwichRule(), self.TensRule(), self.MarriageRule()]