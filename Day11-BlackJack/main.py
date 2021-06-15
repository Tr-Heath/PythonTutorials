#Blackjack game on the console
import deckbuilder
from art import logo

d = deckbuilder.CardDeck()
print(logo)
d.shuffle()
print(d.deck)