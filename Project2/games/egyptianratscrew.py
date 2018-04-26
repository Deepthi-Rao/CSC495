from game_abstractions.game import Game
import rules.ers_rules
from persistent.deck import Deck

class EgyptianRatScrew(Game):
    def __init__(self, players):
        super.declareGame("Egyptian Rat Screw")
        super.declareRules(rules.ers_rules.getAllRules())
        super.createDeck(Deck(Deck.getDefaultDeck()['ranks'], Deck.getDefaultDeck()['suits']))
        super.setPlayers(players)
    