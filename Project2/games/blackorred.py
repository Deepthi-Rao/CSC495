from game_abstractions.game import Game
from persistent.deck import Deck
from rules.blackorred_rules import BlackOrRedRules

class BlackOrRed(Game):
    def __init__(self, players):
        super.declareGame("Black or Red")
        super.declareRules(BlackOrRedRules.getAllRules())
        super.createDeck(Deck.getDefaultDeck()['ranks'], Deck.getDefaultDeck()['suits'])
        super.setPlayers(players)
        
    def play(self):
        pass