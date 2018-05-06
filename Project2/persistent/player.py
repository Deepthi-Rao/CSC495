from persistent.hand import Hand

class Player:

    def __repr__(self):
        return self.name
        
    def __init__(self, playername):
        self.name = playername
        self.hand = Hand()
        self.points = 0
    
    def getName(self):
        return self.name
    
    def viewHand(self):
        if self.hand == None:
            return "Empty hand."
        return str(self.hand)
        
    def getHand(self):
        return self.hand

    def numCards(self):
        return self.hand.getNumCards()
    
    def getCardsInHand(self):
        return self.hand.getCards()
    
    def setHand(self, hand):
        self.hand = hand

    def playTopCard(self):
        return self.hand.playCard()
    
    def playCard(self, card):
        if card in self.hand.getCards():
            return self.hand.discard(card)

    def getPoints(self):
        return self.points
    
    def scorePoint(self):
        self.points += 1
    
    def scorePoints(self, points):
        self.points += points

