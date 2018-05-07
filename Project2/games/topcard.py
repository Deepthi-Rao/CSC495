from game_abstractions.game import Game
from persistent.deck import Deck
from rules.topcard_rules import TopCardRules
from machines.topcard_machine import TopCardMachine
from machine_abstractions.statemachine import StateMachine

class TopCard(Game):
    def __init__(self):
        super().__init__()
        self.declareGame("Top Card")
        self.declareRules(TopCardRules().getAllRules())
        self.createDeck(Deck(Deck.getDefaultDeck()['ranks'], Deck.getDefaultDeck()['suits']))
        self.turnIndex = 0
        
    def play(self):
        self.begin()
        
        while not self.machine.getCurrentState() == StateMachine.Win:
            self.checkDeck(1)
            self.cardPlayed = self.deck.draw()
            self.pile.placeOnTop(self.cardPlayed)
            print("Current Player: " + self.getCurrentPlayer().name)
            print("The dealer has drawn a card.\n")
            print("Active Card: " + self.cardPlayed.__str__() + "\n")
            
            print("Your Hand: " + self.getCurrentPlayer().viewHand())
            print("Which card(s) would you like to play?")
            print("Enter the card numbers with 1 being the first card, separated by spaces.\n")
            cardsIndices = [int(c) for c in input().split()]
            try:
                cards = [self.getCurrentPlayer().hand.getCard(i-1) for i in cardsIndices]
            except:
                print("That was a stupid number. Your turn is over.")
                continue
            
            cards = [self.cardPlayed] + cards
            
            if self.machine.currentState.check(cards):
                print("Card(s) accepted! Your turn has ended.")
                cards = cards[1:]
                [self.getCurrentPlayer().playCard(c) for c in cards]
                
                if self.machine.currentState.checkWin():
                    break
                
            else:
                print("Those cards do not add up to " + str(self.cardPlayed.getRank))
                self.checkDeck(2)
                self.getCurrentPlayer().hand.addCards(self.deck.deal(2))
                print("You have drawn 2 cards. Your turn has ended.")
            self.pile.placeManyOnTop(cards[1:])
            self.machine.currentState.setNextPlayer()
            
        print(self.winner.name + " has won the game!")
            
    
    def begin(self):
        print("____Welcome to Top Card____\n\n")
        print("RULES:")
        print("The dealer will draw a card.")
        print("The player must play up to three cards that add up to the value of the dealer's card.")
        print("If the player cannot, they must draw two cards.")
        print("Whichever player gets an empty hand first wins.")
        print("Good luck!\n\n")
        
        names = []
        numPlayers = int(input("How many players? "))
        for _ in range(numPlayers):
            names.append(input("Enter a name: "))
        
        self.createPlayers(names)
        self.initializeMachine(TopCardMachine(self, self.players))
        self.dealCards(5)
        
TopCard().play()