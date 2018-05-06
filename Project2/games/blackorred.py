from game_abstractions.game import Game
from persistent.deck import Deck
from rules.blackorred_rules import BlackOrRedRules
from persistent.player import Player
from machines.bor_machine import BoRMachine

class BlackOrRed(Game):
    def __init__(self):
        super.declareGame("Black or Red")
        super.declareRules(BlackOrRedRules.getAllRules())
        super.createDeck(Deck.getDefaultDeck()['ranks'], Deck.getDefaultDeck()['suits'])
        
        
    def play(self):
        self.begin()
        
        while self.deck.size > 0:
            self.cardPlayed = self.deck.draw()
            print("The dealer has drawn a card. Black or Red?\n")
            guess = input("Black or Red?\n")
            self.machine.getCurrentState().check(self.cardPlayed, guess)
        
        
    def begin(self):
        print("____Welcome to Black or Red____\n\n")
        print("RULES:")
        print("The dealer will draw a card.")
        print("The player will guess black or red.")
        print("If they are correct, they can go again.")
        print("If they are correct three times in a row, the next player guesses.")
        print("If not, they get points equal to how many guesses they've done, and the next player guesses.")
        print("The game ends when no cards are left to guess.")
        print("The player with the least points wins.")
        print("Good luck!\n\n")
        
        names = []
        numPlayers = input("How many players? ")
        for _ in range(numPlayers):
            names.append(input("Enter a name: "))
        
        players = [Player(n) for n in names]
        super.setPlayers(players)
        
        self.initializeMachine(BoRMachine(self, self.players))
        
        