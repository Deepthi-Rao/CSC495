from game_abstractions.game import Game
from rules.ers_rules import ERSRules
from persistent.deck import Deck
from machines.ersMachine import ERSMachine
from persistent.player import Player
from utils.stack import Stack

class EgyptianRatScrew(Game):
    #this sets up the environment for the game
    def setEnv(self):
        self.declareGame("Egyptian Rat Screw")
        self.declareRules(ERSRules().getAllRules())
        self.createDeck(Deck(Deck.getDefaultDeck()['ranks'], Deck.getDefaultDeck()['suits']))
        self.initializeMachine(ERSMachine(self))
        self.slapQueue = Stack()

    # this creates the players
    def setPlayers(self, playersStr):
        self.createPlayers(playersStr)

    def begin(self):
         self.setCurrentPlayer()
         self.dealCards()

    def play(self):
        self.cardPlayed = self.currentPlayer.playTopCard()
        self.machine.currentState.check(self.cardPlayed)

    def slap(self):
        print(self.currentPlayer + "has slapped the pile!")
        if(isinstance(self.machine.currentState, self.machine.NonSlappable)):
            print("Invalid move! Pile cannot be slapped")
        else:
            self.slapQueue.enqueue(self.currentPlayer)

    def buildEnvironment(self):
        print("____Welcome to Egyptian Rats Crew____")
        print("")
        print("")
        name = input("Please enter the Name of the Player:")
        print("")
        print("")
        print("Hello " + name + ", you will be playing against a computer today. Press 'P' and enter"
                                "to play a card and 'S' and enter, to slap and the pile. Type 'Q' and enter to quit"
                                "Good Luck!")

        names = [name, "computer"]

        game = EgyptianRatScrew()
        game.setEnv()
        game.setPlayers(names)
        game.begin()

        command = input("Enter Command 'P', 'S' or 'Q':")

        while(command != 'Q || q'):
            if(command == 'p' or command == 'P'):
                game.play()
            elif(command == 's' or command == 'S'):
                game.slap()
            else:
                print("Command Not Recognized, try again!")

            command = input("Enter Command 'P', 'S' or 'Q':")








