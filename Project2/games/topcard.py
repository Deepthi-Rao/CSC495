from game_abstractions.game import Game
from persistent.deck import Deck
import rules.topcard_rules

class TopCard(Game):
    def __init__(self, players):
        super.declareGame("Top Card")
        super.declareRules(rules.topcard_rules.getAllRules())
        super.createDeck(Deck.getDefaultDeck()['ranks'], Deck.getDefaultDeck()['suits'])
        super.setPlayers(players)
        
    def play(self):
        pass