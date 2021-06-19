import deckbuilder

CardDeck = deckbuilder.CardDeck()

CardDeck.shuffle()

def printdeck():
    for card in CardDeck.deck:
        print(card)

printdeck()