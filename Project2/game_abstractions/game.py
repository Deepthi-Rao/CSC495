class Game:
    
    def __init__(self):
        self.name, self.players, self.deck, self.rules = None
        
    def declareGame(self, name):
        self.name = name
    
    def declareRules(self, rules):
        self.rules = rules
    
    def createDeck(self, deck):
        self.deck = deck
        
    def setPlayers(self, players):
        self.players = players
        
    # specific to each game
    def play(self):
        pass