from game_abstractions.game import Game
from rules.ers_rules import ERSRules
from persistent.deck import Deck

class EgyptianRatScrew(Game):
    def __init__(self, players):
        super.declareGame("Egyptian Rat Screw")
        super.declareRules(ERSRules())
        super.createDeck(Deck([2,3,4,5,6,7,8,9,10,"J","Q","K","A"],["Hearts","Diamonds","Spades","Clubs"]))
        super.setPlayers(players)
    