from game_abstractions.game import Game
from persistent.deck import Deck
import rules.blackorred_rules

class BlackOrRed(Game):
    def __init__(self, players):
        super.declareGame("Black or Red")
        super.declareRules(rules.blackorred_rules.getAllRules())
        super.createDeck(Deck.getDefaultDeck()['ranks'], Deck.getDefaultDeck()['suits'])
        super.setPlayers(players)