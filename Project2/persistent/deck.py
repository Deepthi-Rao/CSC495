from persistent.card import Card
from utils.stack import Stack

class Deck(Stack):
    def __repr__(self):
        return self.__class__.__name__
        
    def __init__(self, ranks, suits, jokers=False):
        self.stack = [Card(rank, suit) for rank in ranks for suit in suits]
        if jokers:
            self.stack.append(Card("Joker", None))
            self.stack.append(Card("Joker", None))
    
    # returns a dictionary with ranks and suits
    @staticmethod        
    def getDefaultDeck():
        return { 'ranks' : [2,3,4,5,6,7,8,9,10,"J","Q","K","A"],
                'suits' : ["HEARTS","DIAMONDS","SPADES","CLUBS"] }
        
    # deals a specified number of cards from the top of the deck
    def deal(self, numCards):
        return [self.pop() for _ in range(numCards)]

    # takes a list of cards to shuffle back into the deck
    def shuffleInCards(self, cards):
        self.stack.extend(cards)
        self.shuffle()

    # returns false if the deck is empty
    def hasCards(self):
        return self.size() > 0

    # returns the top card of the deck
    def draw(self):
        return self.pop()

    # returns the number of cards remaining in the deck
    def getNumCards(self):
        return self.size()
