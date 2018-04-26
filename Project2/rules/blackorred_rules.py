from rules_abstractions.twoCardRule import TwoCardRule

def getColor(card):
    if card.getSuit() == "HEARTS" or card.getSuit() == "DIAMONDS":
        return "RED"
    else:
        return "BLACK"

# Guessing is the only play in Black Or Red
class GuessRule(TwoCardRule):
    
    # compCard is the drawn card
    # guess is the player's guess of its color
    def canPlay(self, compCard, guess):
        if getColor(compCard) == guess.upper():
            return True
        return False
    
def getAllRules():
    return GuessRule