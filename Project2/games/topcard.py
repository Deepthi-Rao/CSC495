from game_abstractions.game import Game
from persistent.deck import Deck
from rules.topcard_rules import TopCardRules

class TopCard(Game):
    def __init__(self, players):
        super.declareGame("Top Card")
        super.declareRules(TopCardRules.getAllRules())
        super.createDeck(Deck.getDefaultDeck()['ranks'], Deck.getDefaultDeck()['suits'])
        super.setPlayers(players)
        
    def play(self):
        pass