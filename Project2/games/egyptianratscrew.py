from game_abstractions.game import Game
from rules.ers_rules import ERSRules
from persistent.deck import Deck
from machines.ersMachine import ERSMachine
from utils.queue import Queue
import random
import time
import asyncio
import aioconsole



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
         self.dealCards()

    def play(self):
        self.cardPlayed = self.currentPlayer.playTopCard()
        self.machine.currentState.check(self.cardPlayed)
        #computer automatically plays after human
        print("")
        print("")
        time.sleep(0.5)
        self.cardPlayed = self.currentPlayer.playTopCard()
        self.machine.currentState.check(self.cardPlayed)
        print("")
        print("")

    def serviceSlap(self):
        if (isinstance(self.machine.currentState, self.machine.NonSlappable)):
            print("Invalid move! Pile cannot be slapped")

        if(self.slapQueue.peek().getName() == "Computer"):
            print("The computer has slapped the pile!")
        else:
            print(self.slapQueue.peek().getName() + " has slapped the pile!")

        self.slapQueue.peek().getHand().addCards(self.pile.removeAll()) #take all cards from pile and put it in players hand

        while(self.slapQueue.notEmpty()): #remove all elements from slap queue
            self.slapQueue.dequeue()



    def build(self, game):
        print("____Welcome to Egyptian Rats Crew____")
        print("")
        print("")
        name = input("Please enter the Name of the Player:")
        print("")
        print("")
        print("Hello " + name + ", you will be playing against a computer today. Press 'P' and enter"
                                "to play a card and 'S' and enter, to slap and the pile. Type 'Q' and enter to quit"
                                "Good Luck!")

        names = [name, "Computer"]


        game.setPlayers(names)
        game.setEnv()
        game.begin()

        print("Enter Command 'P', 'S' or 'Q':")

        """"#from stack overflow https://stackoverflow.com/questions/35223896/listen-to-keypress-with-asyncio

        command = None
        async def echo():
            stdin = await aioconsole.get_standard_streams()
            async for line in stdin:
                command = line
        loop = asyncio.get_event_loop()
        loop.run_until_complete(echo()) """

        command = input("Enter command")
        while(command != 'Q || q'):
            if(command == 'p\n' or command == 'P\n'):
                game.play()

            elif(command == 's\n' or command == 'S\n'):
                game.slapQueue.enqueue(game.players[0])
            else:
                print("Command Not Recognized, try again!")
                continue


            #computer playing
            if(isinstance(self.machine.currentState, self.machine.Slappable)):
                slapFreq = random.randint(1,10)
                if(slapFreq > 2):
                    timeFreq = random.randint(1, 4)
                    time.sleep(timeFreq)
                    game.slapQueue.enqueue(game.players[1])

            if(game.slapQueue.notEmpty()):
                game.serviceSlap()








#starts game.
game = EgyptianRatScrew()
game.build(game)





