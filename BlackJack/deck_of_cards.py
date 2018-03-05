""" 

    Blackjack 
    
    by Byron Luo
"""

import random
suit_names = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
rank_names = ('Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King')

card_val = {'Ace':1,'2':2, '3':3, '4':4, 
    '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

class Card:
    
    # Initialize suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def show(self):
        print ("{} of {}".format(self.rank, self.suit))
        
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in suit_names:
            for v in range(1,14):
                self.cards.append(Card(s,v))
                
    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            # Python Swap
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()
        
class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []
        
        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self  ## python chaining
        
    def showHand(self):
        for card in self.hand:
            card.show()
    def discard(self):
        return self.hand.pop()

deck = Deck()
deck.shuffle()
deck.show()
#deck = Deck()
#deck.shuffle()
#deck.show()
bob = Player('Bob')
bob.draw(deck)
bob.showHand()
#bob.discard()
#bob.showHand()




        


        
