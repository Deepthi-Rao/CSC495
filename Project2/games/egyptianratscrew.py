from game_abstractions.game import Game
from rules.ers_rules import ERSRules
from persistent.deck import Deck
from machines.ersMachine import ERSMachine
from persistent.player import Player


class EgyptianRatScrew(Game):
    def __init__(self, players):
        self.declareGame("Egyptian Rat Screw")
        self.declareRules(ERSRules().getAllRules())
        self.createDeck(Deck(Deck.getDefaultDeck()['ranks'], Deck.getDefaultDeck()['suits']))
        self.setPlayers(players)
        self.machine = ERSMachine(self, self.players, self.rules, self.deck)

    def play(self):
        currentCard = self.machine.currentPlayer.playTopCard()
        self.machine.currentState.check(currentCard)

playersID = ["hello", "jimmy"]
players = [Player(p) for p in playersID]
currentGame = EgyptianRatScrew(players)
currentGame.play()

