from persistent.hand import Hand
from persistent.player import Player
from persistent.deck import Deck
from persistent.pile import Pile

class Game:
    
    def __init__(self):
        self.name = None
        self.machine = None
        self.deck = None
        self.pile = Pile()
        self.currentPlayer = None
        self.cardPlayed = None
        self.players = []
        self.rules = []
        self.turnIndex = 0

    #initialize game specific machine
    def initializeMachine(self, machine):
        self.machine = machine

    #creates the players according to the string passed in
    def createPlayers(self, playersStr):
        self.players = [Player(p) for p in playersStr]

    # set the current player
    def setCurrentPlayer(self):
        self.currentPlayer = self.players[self.turnIndex % len(self.players)]

    # deals all cards in the deck to all players defined
    def dealCards(self):
        size = self.deck.size()
        while (size):
            self.players[self.deck.size() % len(self.players)].getHand().addCard(self.deck.pop())
            size = size - 1

    #this declares the game
    def declareGame(self, name):
        self.name = name

    # this declares the rules
    def declareRules(self, rules):
        self.rules = rules

    # this creates the deck
    def createDeck(self, deck):
        self.deck = deck
        self.deck.shuffle()

    # this increments the turn index
    def incrementTurnIndex(self):
        self.turnIndex = self.turnIndex + 1

    # specific to each game
    def play(self):
        pass