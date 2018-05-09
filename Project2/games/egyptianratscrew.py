from game_abstractions.game import Game
from rules.ers_rules import ERSRules
from persistent.deck import Deck
from machines.ersMachine import ERSMachine
from utils.queue import Queue
import random
import time



class EgyptianRatScrew(Game):

    #this sets up the environment for the game
    def setEnv(self):
        self.declareGame("Egyptian Rat Screw")
        self.declareRules(ERSRules().getAllRules())
        self.createDeck(Deck(Deck.getDefaultDeck()['ranks'], Deck.getDefaultDeck()['suits']))
        self.initializeMachine(ERSMachine(self))
        self.slapQueue = Queue()

    # this creates the players
    def setPlayers(self, playersStr):
        self.createPlayers(playersStr)

    def begin(self):
         self.setCurrentPlayer()
         self.dealAllCards()

    def play(self):
        self.cardPlayed = self.currentPlayer.playTopCard()
        self.machine.currentState.check(self.cardPlayed)

    def serviceSlap(self):
        print("")
        print("")
        print(self.slapQueue.peek().getName() + " has slapped the pile!")
        print(self.displayMessage)
        self.slapQueue.peek().getHand().addCards(self.pile.removeAll())  # take all cards from pile and put it in players hand
        print(self.slapQueue.peek().getName() + " has " + str(self.slapQueue.peek().getHand().size()) + " cards in hand.")
        print("")
        print("")


        while(self.slapQueue.notEmpty()): #remove all elements from slap queue
            self.slapQueue.dequeue()

    def build(self, game):
        print("____Welcome to Egyptian Rats Crew____")
        print("")
        print("")

        names = ["Hanna", "Deepthi"]

        game.setPlayers(names)
        game.setEnv()
        game.begin()

        while( not isinstance(game.machine.currentState, self.machine.Win)):

            game.play()

            if (isinstance(self.machine.currentState, self.machine.Slappable)):
                slapFreq = random.randint(1, 10)
                if (slapFreq > 2):
                    slap = random.randint(0, 1)
                    if(slap == 0):
                        game.slapQueue.enqueue(game.players[0])
                    else:
                        game.slapQueue.enqueue(game.players[1])

            if(game.slapQueue.notEmpty()):
                game.serviceSlap()


#starts game. uncomment to see the game functionality
#game = EgyptianRatScrew()
#game.build(game)





