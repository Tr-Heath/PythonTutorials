#Deck Builder for card games
import random

class CardDeck:
    #todo: Some games need rankings for face cards ie. a Queen outranks a Jack.
    card_values = {
            "Two":2,
            "Three":3,
            "Four":4,
            "Five":5,
            "Six":6,
            "Seven":7,
            "Eight":8,
            "Nine":9,
            "Ten":10,
            "Jack":10,
            "Queen":10,
            "King":10,
            "Ace":11
    }

    card_suits = ["Spades", "Diamonds", "Clubs", "Hearts" ]

    deck = []

    def __init__(self):
        for cardvalue in self.card_values:
            for cardsuit in self.card_suits:
                self.deck.append([{cardvalue: self.card_values[cardvalue]},cardsuit])
    
    def shuffle(self):
        '''Based on Fisher-Yates shuffle and as demonstrated by Donald Knuth in The Art of Computer Programming 2. Seminumerical algorithms.'''
        n = 51 #TODO could pass in value here for non-standard decks
        for card in self.deck:
            k = random.randint(0, n + 1) # random number less than n + 1
            temp = self.deck[k]
            self.deck[k] = self.deck[n]
            self.deck[n] = temp
            n -= 1
    
    def drawcard(self):
        if(len(self.deck) > 0):
            return self.deck.pop()