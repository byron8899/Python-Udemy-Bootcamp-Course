#Blackjack 
#by Byron Luo


import random
import time



chip_amount = 100

bet_flag = 1
playing = 1
# Hearts, Diamonds, Clubs, Spades
suit_names = ('H', 'D', 'C', 'S')
rank_names = ('Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King')

# Map Dictionaries for 10
card_val = {'Ace':1,'2':2, '3':3, '4':4, 
    '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}


# Create the model of a card
class Card(object):
    # attributes are suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    # prints a string
    def __str__(self):
        return self.suit + self.rank

    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank
    def draw(self):
        print(self.suit + self.rank)
    
class Deck(object):
    def __init__(self):
        self.deck = []
        for suit in suit_names:
            for rank in rank_names:
                self.deck.append(Card(suit,rank))
    
    def shuffle(self):
        '''Shuffle the deck'''
        random.shuffle(self.deck)
    def __str__(self):
        
        deck_string = ""
        
        for card in self.deck:
            deck_string += " " + card.__str__()
            
        return "The deck has" + deck_string
    
    # grab a single deck from 52 cards
    def deal(self):
        return self.deck.pop()
                

class Hand(object):
    def __init__(self):
        self.cards = []
        self.value = 0
        # Aces can be 1 or 11
        self.ace = False
        
    def addCard(self, card):
        self.cards.append(card)
        
        if (card.rank == 'Ace'):
            self.ace = True
        self.value = self.value + card_val[card.rank]
        
    def calc_val(self):
        if(self.ace == True and self.value < 12):
            return self.value + 10
        else:
            return self.value
        
    def __str__(self):
        cards_string = ""
        for card in self.cards:
            cards_string += " " + card.__str__()
        
        return "The hand has" + cards_string
    
    # This function disables a single card (For the dealer only until the player stands)
    
    def draw(self,hidden):
        if hidden == True:
            # First hidden card is not shown
            starting_card = 1
        
        else:
            starting_card = 0
        
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()
            
        
def intro():
    
    statement = """Welcome to BlackJack!\nThis is Byron's first python project.\n
Have fun and win money"""
    print(statement)

def makeBet():
    global bet_flag, chip_amount
    bet_flag = 0
    
    print('You currently have ${}.'.format(chip_amount))
    print('Please make a bet (Whole Integers only)')
    
    # if an acceptable amount has been entered, bet_flag sets to another number to exit loop.
    while(bet_flag == 0):
        inputBet = int(input())
        
        if (inputBet <= chip_amount and inputBet > 0):
            # Exits the while loop
            bet_flag = inputBet
            
            print('You bet ${}.'.format(inputBet))
        
        else:
            if(inputBet == 0):
                print("Error: Please enter the appropriate amount")
            else:
                print("Error: You have ${}. You don't have enough money to play.".format(chip_amount))
                print("Please try again.")
                


def dealCards():
    print ('Dealing Cards')
    global deck
    deck = Deck()
    deck.shuffle()
    
    makeBet()
    
    player_hand = Hand() 
    dealer_hand = Hand()

    
    player_hand.addCard(deck.deal())
    player_hand.addCard(deck.deal())
    
    dealer_hand.addCard(deck.deal())
    dealer_hand.addCard(deck.deal())
    
    # Player calls game_on to play
    game_on(player_hand, dealer_hand)
    
def game_on(player_hand,dealer_hand):
    
    global deck
    
    print('')
    
    print('You have: ')
    player_hand.draw(hidden = False)
    print('Total: {}'.format(player_hand.calc_val()))

    
    print('''Dealer's hand has: ''')
    dealer_hand.draw(hidden = True)
    
    # Checks if the player hand has a blackjack
    if(player_hand.calc_val() == 21):
        print('Player got Blackjack')
        player_stand(player_hand,dealer_hand)
        
    # If not, player makes a choice on hitting or standing
    else:
        print("Press 'h' to hit or press 's' to stand")
        
        player_input = input()
        
        if(player_input == 'h'):
            player_hit(player_hand,dealer_hand)
        elif (player_input == 's'):
            player_stand(player_hand,dealer_hand)
        else:
            pass
        
    
def player_hit(player_hand,dealer_hand):
    global deck, playing, chip_amount, bet_flag
    
    player_hand.addCard(deck.deal())
    
    
    # checks for player's bust
    if (player_hand.calc_val() > 21):
        print('')
        print('You have: ')
        player_hand.draw(hidden = False)
        print('')
        print('***********************')
        print('Busted! Sorry You lose')
        print('***********************')
        
        print('You lost ${}.'.format(bet_flag))
        
        chip_amount -=bet_flag
        startAgain()
        
    elif (player_hand.calc_val() == 21):
        player_stand(player_hand,dealer_hand)
        
        
    else:
        game_on(player_hand,dealer_hand)

def player_stand(player_hand,dealer_hand):
    
    global deck, playing, chip_amount, bet_flag
    
    print('''Dealer's hand has: ''')
    dealer_hand.draw(hidden = False)
    time.sleep(1)
    print('')
    while (dealer_hand.calc_val()) < 17:
        
        dealer_hand.addCard(deck.deal())
        dealer_hand.draw(hidden = False)
        time.sleep(1)
    
    if (dealer_hand.calc_val() < 22):
        if (player_hand.calc_val() > dealer_hand.calc_val()):
            print("*******")
            print('You win')
            print("*******")
            print('')
            chip_amount += bet_flag
            startAgain()
        elif (player_hand.calc_val() == dealer_hand.calc_val()):
            print("****")
            print('Push')
            print('****')
            print('')
            print('You have ${} left.'.format(chip_amount))
            
            startAgain()
        else:
            print("***********************")
            print('Dealer Wins, you lose')
            print("***********************")
            print('You lost ${}.'.format(bet_flag))
            chip_amount -=bet_flag
            print('')
            print('You have ${} left.'.format(chip_amount))
            
            startAgain()
    else:
        print("*************")
        print('Dealer Busts')
        print("*************")
        chip_amount += bet_flag
        startAgain()
    
#Player chooses whether he/she wants to play again or not
def startAgain():
    global playing, chip_amount
    if chip_amount == 0:
        print('You have no money left')
        playing = 0
    else:
        print('''Would you like to play again? 'Y' or 'N'?''')
        inputChoice = input().lower()
        
        if (inputChoice == 'y'):
            bet_flag = 0
            dealCards()
        else:
            #quits the game
            playing = 0
    

    
intro()    
while(playing == 1):
    dealCards()

print("Thanks for playing")
time.sleep(2)









