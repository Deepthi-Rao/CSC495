from game_abstractions.game import Game
from persistent.deck import Deck
from rules.blackorred_rules import BlackOrRedRules
from machines.bor_machine import BoRMachine

class BlackOrRed(Game):
    def __init__(self):
        super().__init__()
        self.declareGame("Black or Red")
        self.declareRules(BlackOrRedRules().getAllRules())
        self.createDeck(Deck(Deck.getDefaultDeck()['ranks'], Deck.getDefaultDeck()['suits']))
        self.turnIndex = 0
        
        
    def play(self):
        self.intro()
        self.initializePlayers()
        
        while self.deck.getNumCards() > 0:
            self.cardPlayed = self.deck.draw()
            print("Current Player: " + self.getCurrentPlayer().name)
            print("The dealer has drawn a card.\n")
            guess = input("Black or Red?\n")
            self.machine.getCurrentState().check(self.cardPlayed, guess)
        
        winner = self.findWinner()
        print(winner.name + " is the winner!")
        
        
    def initializePlayers(self):
        names = []
        numPlayers = int(input("How many players? "))
        for _ in range(numPlayers):
            names.append(input("Enter a name: "))
        
        self.createPlayers(names)
        self.initializeMachine(BoRMachine(self, self.players))
        
    def findWinner(self):
        print("No cards remaining. Finding the winner...")
        print("...")
        print("...")
        print("...")
        
        lowest = self.players[0]
        for p in self.players:
            if p.getPoints() < lowest.getPoints():
                lowest = p
        return lowest

    def intro(self): 
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
        
BlackOrRed().play()
        