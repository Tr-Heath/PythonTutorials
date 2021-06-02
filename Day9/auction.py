<<<<<<< HEAD
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
=======
#Day 9, working with dictionaries in Python, exercised with simple auction tracking app

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])
>>>>>>> e034c5b6e25c0dede389ffbb1b4b6088b19fb4f8
