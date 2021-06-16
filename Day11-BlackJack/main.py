#Blackjack game on the console
import deckbuilder
from art import logo


class BlackJack:
    cardDeck = []
    dealerHand = []
    playerHand = []
    playerBank = 0

    def __init__(self):
        self.cardDeck = deckbuilder.CardDeck()
        self.dealerHand = []
        self.playerHand = []
        self.playerBank = 1000

    def deal():
        if len(self.cardDeck.deck) > 3:
            game.dealerHand.append(d.drawcard())
            game.playerHand.append(d.drawcard())
            game.playerHand.append(d.drawcard())
        else:
            d = deckbuilder.CardDeck()
            d.shuffle()


game = BlackJack()
print(logo)
d.shuffle()

def calculate_hand(hand):

print(game.playerBank)
print(d.drawcard())
