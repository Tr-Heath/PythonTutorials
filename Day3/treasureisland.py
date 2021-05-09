print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

def forkInTheRoad():
    roadChoice = input("You are at a fork in the road, would you like to go left or right? ")
    if roadChoice == "left":
        lakeApproach()
    else:
        gameOver("You fell in a hole. ")
def lakeApproach():
    lakeChoice = input("You come to a lake. There is an island in the middle of the lake. Would you like to wait for a boat or swim? Type \"wait\" or \"swim\". ")
    if lakeChoice == "wait":
        lakeHouse()
    else:
        gameOver("You were eaten by a shark. ")
def lakeHouse():
    houseChoice = input("You arrive at the lake house unharmed. The building has three doors. They are colored red, blue, yellow. Enter the color of the door to enter. ")
    if houseChoice == "yellow":
        print("You found the treasure and win the game!")
    elif houseChoice == "blue":
        gameOver("You were eaten by a beast. ")
    else:
        gameOver("Fell into fire. ")

def gameOver(reason):
    print(reason + " Game over.")

forkInTheRoad()