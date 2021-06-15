#Deck Builder for card games
import random

class CardDeck:

    card_values = {
            2: "Two",
            3 : "Three",
            4 : "Four",
            5 : "Five",
            6 : "Six",
            7 : "Seven",
            8 : "Eight",
            9 : "Nine",
            10 : "Ten",
            11 :"Jack",
            12 : "Queen",
            13 : "King",
            1  : "Ace"
    }

    card_suits = ["Spades", "Diamonds", "Clubs", "Hearts" ]

    deck = []

    def __init__(self):
        for cardvalue in self.card_values:
            for cardsuit in self.card_suits:
                self.deck.append([cardvalue,cardsuit])
    
    def shuffle(self):
        '''Based on Fisher-Yates shuffle and as demonstrated by Donald Knuth in The Art of Computer Programming 2. Seminumerical algorithms.'''
        n = 51 #TODO could pass in value here for non-standard decks
        for card in self.deck:
            k = random.randint(0, n + 1) # random number less than n + 1
            temp = self.deck[k]
            self.deck[k] = self.deck[n]
            self.deck[n] = temp
            n -= 1