from persistent.hand import Hand
from persistent.player import Player

class Game:
    
    def __init__(self):
        self.name, self.players, self.deck, self.rules = None
        
    def declareGame(self, name):
        self.name = name
    
    def declareRules(self, rules):
        self.rules = rules
    
    def createDeck(self, deck):
        self.deck = deck

    def createPlayers(self, playersStr):
        self.players = [Player(p) for p in playersStr]

    def setPlayers(self, players):
        for p in self.players:
            p.setHand(Hand(self.deck.deal()))

    # specific to each game
    def play(self):
        pass