from rules_abstractions.twoCardRule import TwoCardRule

class BlackOrRedRules:

    def __init__(self):
        self.rules = self.getAllRules();

    # Guessing is the only play in Black Or Red
    class GuessRule(TwoCardRule):

        # compCard is the drawn card
        # guess is the player's guess of its color
        def canPlay(self, compCard, guess):
            if self.getColor(compCard) == guess.upper():
                return True
            return False

        @staticmethod
        def getColor(card):
            if card.getSuit() == "HEARTS" or card.getSuit() == "DIAMONDS":
                return "RED"
            else:
                return "BLACK"

    def getAllRules(self):
        return [self.GuessRule]