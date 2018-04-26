from utils.stack import Stack

# a Pile is a representation of the in-play pile of cards, with behaviour inherited from Stack
class Pile(Stack):
    
    # initializes the pile
    def __init__(self):
        self.stack = []

    # empties the pile and returns a list of the cards from it
    def takeAllCards(self):
        cards = self.stack
        self.stack = []
        return cards    

    # adds a card to the top of the stack
    def placeOnTop(self, card):
        self.push(card)
