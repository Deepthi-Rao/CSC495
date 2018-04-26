from game_abstractions.game import Game
import rules.ers_rules
from persistent.deck import Deck

class EgyptianRatScrew(Game):
    def __init__(self, players):
        super.declareGame("Egyptian Rat Screw")
        super.declareRules(rules.ers_rules.getAllRules())
        super.createDeck(Deck([2,3,4,5,6,7,8,9,10,"J","Q","K","A"],["HEARTS","DIAMONDS","SPADES","CLUBS"]))
        super.setPlayers(players)
    