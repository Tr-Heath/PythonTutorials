#Blackjack game on the console
import deckbuilder
from art import logo


class BlackJack:
    cardDeck = []
    dealerHand = []
    playerHand = []
    playerBank = 0

    def __init__(self):
        '''game start should initialize a Deck of cards, empty player and dealer hands to hold each
        round. Additionally, the player's bank should default. Future enhancement to create a save game'''
        self.cardDeck = deckbuilder.CardDeck()
        self.cardDeck.shuffle()
        self.dealerHand = []
        self.playerHand = []
        self.playerBank = 1000

    def deal(self):
        if len(self.cardDeck.deck) > 4:
            self.dealerHand.append(self.cardDeck.drawcard())
            self.dealerHand.append(self.cardDeck.drawcard())
            self.playerHand.append(self.cardDeck.drawcard())
            self.playerHand.append(self.cardDeck.drawcard())
        else:
            self.cardDeck = deckbuilder.CardDeck()
            self.cardDeck.shuffle()
            self.deal()

    def calculate_hand(self, hand):
        '''tally up total value for a given list of cards
        If total exceeds 21, check if an Ace exists and retry calculuation 
        using the value of the ace as 1 instead of 11. '''
        handtotal = 0
        for card in hand:
            handtotal += int(sum(card[0].values()))
        #if total is over 21, check if it is only a soft bust
        if handtotal > 21:
            handtotal = 0
            for card in hand:
                if card[0].values() == 11:
                    handtotal += 1
                else:
                    handtotal += int(sum(card[0].values()))
        return handtotal

    def printhand(self, hand, isDealer):
        display = ""
        if isDealer :
            print(f"Dealer shows {list(hand[0][0].keys())[0]} of {hand[0][1]}")
        else:
            for card in hand:
                value = card[0]
                suit = card[1]
                display += f"{list(card[0].keys())[0]} of {card[1]}, "
            print(f"You have {display}")

    def hit(self, isDealer):
        if(isDealer):
            self.dealerHand.append(self.cardDeck.drawcard())
        else:
            self.playerHand.append(self.cardDeck.drawcard())
        

game = BlackJack()
print(logo)
game.deal()

game.printhand(game.playerHand, False)
playertotal = game.calculate_hand(game.playerHand)
game.printhand(game.dealerHand, True)
dealertotal = game.calculate_hand(game.dealerHand)
game.hit(False)
game.printhand(game.playerHand, False)
print(playertotal)
print(dealertotal)
print(game.playerBank)
