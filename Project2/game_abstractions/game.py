from persistent.player import Player
from persistent.pile import Pile

class Game:
    
    def __init__(self):
        self.name, self.machine, self.deck = None
        self.currentPlayer, self.cardPlayed, self.winner = None
        self.players, self.rules = [], []
        self.pile = Pile()
        self.turnIndex = 0
        self.displayMessage = ""

    #initialize game specific machine
    def initializeMachine(self, machine):
        self.machine = machine

    #creates the players according to the string passed in
    def createPlayers(self, playersStr):
        self.players = [Player(p) for p in playersStr]

    # set the current player
    def setCurrentPlayer(self, player = None):
        if player == None:
            self.currentPlayer = self.players[self.turnIndex % len(self.players)]
        else:
            self.currentPlayer = player
            
    def getCurrentPlayer(self):
        return self.currentPlayer


    # deals all cards in the deck to all players defined
    def dealAllCards(self):
        size = self.deck.size()
        while (size):
            self.players[self.deck.size() % len(self.players)].getHand().addCard(self.deck.pop())
            size = size - 1
            
    def dealCards(self, handSize):
        if handSize * len(self.players) > 54:
            raise Exception('Hand size too large')
        else:
            for p in self.players:
                p.getHand().addCards(self.deck.deal(handSize))

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
        
    def checkDeck(self, numCards):
        if self.deck.size() - numCards <= 0:
            self.deck.shuffleInCards(self.pile.takeAllCards())

    # specific to each game
    def play(self):
        pass