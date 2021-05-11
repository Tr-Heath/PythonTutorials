#Warm up exercise leveraging randomization functionality in python. 
import random, gameimages

#pass an int 0-2 and return image of choice
# def choiceImage(image):
#     if int(image) == 0:
#         return gameimages.rock
#     elif int(image) == 1:
#         return gameimages.paper
#     else:
#         return gameimages.scissors

def winCondition(computer, player):
    if(computer == player):
        print("Tie! Try again!")
    elif(gameimages.game_images[computer] == gameimages.game_images[player-1]):
        print("You win!")
    else: 
        print("You lose!")

print("Welcome to the game rock, paper scissors!")
player = int(input("Please type your choice. '0' for rock, '1' for paper and '2' for scissors."))
computerChoice = random.randint(0,2)
#compImage = choiceImage(random.randint(0, 2))
#playerImage = choiceImage(choice)

print(f"You have chosen:")
print(gameimages.game_images[player])
print("Computer has:")
print(gameimages.game_images[computerChoice])
winCondition(computerChoice, player)
