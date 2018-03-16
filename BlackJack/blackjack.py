# Blackjack Project (Practice)
# by Byron Luo
# Create to Jose Portilla from Python Complete Bootcamp

import random
import time



chip_amount = 100
# Hearts, Diamonds, Clubs, Spades
suit_names = ('Hearts', 'Diamonds', 'Club', 'Spade')
rank_names = ('Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King')

# Map Dictionaries for 10
card_val = {'Ace':1,'2':2, '3':3, '4':4, 
    '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}


''' Create the model of a card '''
class Card(object):
    # attributes are suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    # prints a string
    def __str__(self):
        return self.suit + " of "+ self.rank

    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank
    def draw(self):
        print(self.suit + ' of ' + self.rank)

''' Create a Model for Deck of cards'''
class Deck(object):
    
    def __init__(self):
        self.deck = []
        for suit in suit_names:
            for rank in rank_names:
                self.deck.append(Card(suit,rank))
    
    def shuffle(self):
        '''Shuffle the deck'''
        random.shuffle(self.deck)
    
    # This is only for checking for cards are listed in the Deck.
    def __str__(self):
        deck_string = ""
        
        for card in self.deck:
            deck_string += " " + card.__str__()
            
        return "The deck has" + deck_string+"\n"
    
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

class betChips(object):
    
    
    def __init__(self,chipTotal):
        self.chipTotal = chipTotal
        self.betInput = 0
    
    def winBet(self):
        self.chipTotal += self.betInput
    def loseBet(self):
        self.chipTotal -= self.betInput     
    # This function disables a single card (For the dealer only until the player stands)
'''  
    def draw(self,hidden):
        if hidden == True:
            # First hidden card is not shown
            starting_card = 1
        
        else:
            starting_card = 0
        
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()
'''           
def intro():
    
    statement = """Welcome to BlackJack!\nThis is Byron's first Python project.\n\
    
Have fun and win money"""
    print(statement)
    print('')

def makeBet(playerBet):
    
    # User enters a bet
    
    
    # if an acceptable amount has been entered, the while loop ends
    while True:
        try:
            print('You currently have ${}.'.format(playerBet.chipTotal))
            print('Please make a bet (Whole Integers only): ')
            playerBet.betInput = int(input())
        except:
            print("Error: Please enter the digits only\n ")
            continue
        else:
            if (playerBet.betInput <= playerBet.chipTotal and playerBet.betInput > 0):
                # Exits the while loop
                print('You bet ${}.'.format(playerBet.betInput))
                break
                '''Ends the while loop'''
            else:
                if(playerBet.betInput == 0):
                    print("Error: Please enter the appropriate amount\n")
                else:
                    print("Error: You have ${}. You don't have enough money to play.\n".format(playerBet.chipTotal))
                    
    
    print(playerBet.betInput)            

'''
def dealCards():
    print ('Dealing Cards')
    deck = Deck()
    deck.shuffle()
    playerBet = betChips()
    makeBet(playerBet)
    
    player_hand = Hand() 
    dealer_hand = Hand()

    
    player_hand.addCard(deck.deal())
    player_hand.addCard(deck.deal())
    
    dealer_hand.addCard(deck.deal())
    dealer_hand.addCard(deck.deal())
    
    # Player calls game_on to play
    game_on(player_hand, dealer_hand,deck, playerBet)
'''    

def game_on(player_hand,dealer_hand,deck, playerBet):
    
    
    print('')
    
    print("\nYou have: ",*player_hand.cards, sep='\n')
    #player_hand.draw(hidden = False)
    print('Total: {}'.format(player_hand.calc_val()))

    print("\nDealer's hand has: ",dealer_hand.cards[1], sep='\n')
    
    # Checks if the player hand has a blackjack
    if(player_hand.calc_val() == 21):
        print('Player got Blackjack')
        player_stand(player_hand,dealer_hand, deck, playerBet)
        
    # If not, player makes a choice on hitting or standing
    else:
        print("Press 'h' to hit or press 's' to stand")
        
        player_input = input()
        
        if(player_input == 'h'):
            player_hit(player_hand,dealer_hand, deck, playerBet)
        elif (player_input == 's'):
            player_stand(player_hand,dealer_hand, deck, playerBet)
        else:
            pass
        
    
def player_hit(player_hand,dealer_hand, deck, playerBet):

    player_hand.addCard(deck.deal())
    
    
    # checks for player's bust
    if (player_hand.calc_val() > 21):
        print('')
        print('You have: ')
        print("\n",*player_hand.cards, sep='\n')
        print('')
        print('***********************')
        print('Busted! Sorry You lose')
        print('***********************')
        
        print('You lost ${}.'.format(playerBet.betInput))
        playerBet.loseBet()
        print('')
        print('You have ${} left.'.format(playerBet.chipTotal))
        #startAgain()
        
    elif (player_hand.calc_val() == 21):
        player_stand(player_hand,dealer_hand, deck, playerBet)
        
        
    else:
        game_on(player_hand,dealer_hand, deck, playerBet)

def player_stand(player_hand,dealer_hand, deck, playerBet):

    
    print("\nDealer's hand has: ",*dealer_hand.cards, sep='\n')
    time.sleep(1)
    print('')
    while (dealer_hand.calc_val()) < 17:
        
        dealer_hand.addCard(deck.deal())
        print("\n: ",*dealer_hand.cards, sep='\n')
        time.sleep(1)
    
    if (dealer_hand.calc_val() < 22):
        if (player_hand.calc_val() > dealer_hand.calc_val()):
            print("*******")
            print('You win')
            print("*******")
            print('')
            playerBet.winBet()
            print('')
            print('You have ${} left.'.format(playerBet.chipTotal))
            #startAgain()
        elif (player_hand.calc_val() == dealer_hand.calc_val()):
            print("****")
            print('Push')
            print('****')
            print('')
            print('You have ${} left.'.format(playerBet.chipTotal) )
            
            #startAgain()
        else:
            print("***********************")
            print('Dealer Wins, you lose')
            print("***********************")
            print('You lost ${}.'.format(playerBet.betInput))
            playerBet.loseBet()
            print('')
            print('You have ${} left.'.format(playerBet.chipTotal))
            
            #startAgain()
    else:
        print("*************")
        print('Dealer Busts')
        print("*************")
        playerBet.winBet()
        print('')
        print('You have ${} left.'.format(playerBet.chipTotal))
        #startAgain()
    

#Player chooses whether he/she wants to play again or not  
def startAgain(playerBet):
    if playerBet.chipTotal == 0:
        print('You have no money left')
        time.sleep(2)
        exit()
    else:
        print('''Would you like to play again? 'Y' or 'N'?''')
        inputChoice = input().lower()
        
        if (inputChoice == 'y'):
            pass
        else:
            print("Thanks for playing")
            time.sleep(2)
            exit()
            
    
intro()
playerBet = betChips(chip_amount)    
while True:
    print ('Dealing Cards')
    deck = Deck()
    deck.shuffle()
    makeBet(playerBet)
    
    player_hand = Hand() 
    dealer_hand = Hand()

    
    player_hand.addCard(deck.deal())
    player_hand.addCard(deck.deal())
    
    dealer_hand.addCard(deck.deal())
    dealer_hand.addCard(deck.deal())
    
    
    game_on(player_hand,dealer_hand,deck, playerBet)
    
    startAgain(playerBet)











