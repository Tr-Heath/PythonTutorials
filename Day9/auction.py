#Blind auction system.
#Ask for bidder name and keep taking max bids from individuals until there are no 
#bidders remaining. Clear the screen after every input bid.

#TODO improvments
#1. See if there are duplicate names
#2. Validate if bid is numeric

import os, platform, auctionlogo

class Auction:
    bids = {}
    currentBidder = ""
    currentBid = 0
    keepBidding = "yes"

    def getBid(self):
        self.clear()
        print(auctionlogo.logo)
        self.currentBidder = input("What is your name? ")
        self.currentBid = int(input("What is your bid? $"))
        self.bids[self.currentBidder] = self.currentBid

    def clear(self):
        if(platform.system() == "Windows"):
            os.system('cls') #Windows clear command for blind auction.
        elif(platform.system() == "Linux"):
            os.system('clear') #Linux clear command for blind auction.
    
    #Validate User input, if they indicate additional entries are needed, continue getting bids, else set term flag.
    def checkContinue(self):
        userIndicator = input("Are there other bidders (Yes/No)? ").lower()
        if userIndicator == "yes":
            self.getBid()
        elif userIndicator == "no":
            self.keepBidding = userIndicator
        else:
            print("Please type \"Yes\" or \"No\"")

    def calculateAuction(self):
        winner = ""
        highestBid = 0
        for key in self.bids:
            if self.bids[key] >= highestBid:
                winner = key
                highestBid = self.bids[key]
        print(f"{winner} is the winner! With a bid of ${self.bids[winner]}")

    def __init__(self):
        pass



a = Auction()

a.getBid()

while a.keepBidding == "yes":
    a.checkContinue()

a.calculateAuction()
