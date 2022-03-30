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
    
    def printDealerHand(self, isEnd):
        display = ""
        if isEnd:
            print("The End")
            for card in self.dealerHand:
                display += f"{list(card[0].keys())[0]} of {card[1]}, "
            print(f"Dealer has {display}")
        else:
            print(f"Dealer shows {list(self.dealerHand[0][0].keys())[0]} of {self.dealerHand[0][1]}")

    def printPlayerHand(self):
        display = ""
        for card in self.playerHand:
            display += f"{list(card[0].keys())[0]} of {card[1]}, "
        print(f"You have {display}")

    def hit(self, isDealer):
        if(isDealer):
            self.dealerHand.append(self.cardDeck.drawcard())
        else:
            self.playerHand.append(self.cardDeck.drawcard())

    def resetHands(self):
        self.playerHand = []
        self.dealerHand = []

game = BlackJack()
print(logo)
playerChoice = "Start"
#print(game.playerBank)

while playerChoice != "Q":
    game.resetHands()
    game.deal()

    game.printPlayerHand()
    game.printDealerHand(False)

    #start choice loop
    while playerChoice != "Q":
        dealertotal = game.calculate_hand(game.dealerHand)
        playertotal = game.calculate_hand(game.playerHand)
        print("What would you like to do?")
        playerChoice = input("Enter \"H\" for Hit, \"S\" for Stay, \"Q\" to stop playing.")
        if playerChoice == "H":
            game.hit(False)
            game.printPlayerHand()
        elif playerChoice == "S":
            print(f"Dealer total is {dealertotal}")
            if dealertotal < 17:
                game.hit(True)
            game.printDealerHand(True)
    #reset


print(playertotal)
print(dealertotal)

