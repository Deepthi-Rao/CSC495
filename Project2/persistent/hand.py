# a representation of a player's hand of cards
class Hand:
    def __repr__(self):
        return ', '.join([str(c) for c in self.cards])
        
    def __str__(self):
        return ', '.join([str(c) for c in self.cards])

    def __init__(self):
        self.cards = []

    # returns the list of cards in the hand
    def getCards(self):
        return self.cards
    
    def getCard(self, idx):
        return self.cards[idx]
    
    # returns the number of cards in the hand
    def getNumCards(self):
        return len(self.cards)

    #add one card to the deck
    def addCard(self, card):
        self.cards.append(card)

    # adds multiple cards to the hand
    def addCards(self, cards):
        self.cards.extend(cards)

    # this gets the first card off the top of the players hand (rightmost index)
    def playCard(self):
        if(len(self.cards) > 0):
            return self.cards.pop()
        pass

    # discards a specific card from the hand    
    def discard(self, card=None, idx=-1):
        if idx == -1:
            if card in self.cards:
                self.cards.remove(card)
                return True
            return False
        else:
            return self.cards.pop(idx)

    #returns the size
    def size(self):
        return len(self.cards)