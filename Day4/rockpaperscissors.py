#Warm up exercise leveraging randomization functionality in python. 
import random, gameimages

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

print(f"You have chosen:")
print(gameimages.game_images[player])
print("Computer has:")
print(gameimages.game_images[computerChoice])
winCondition(computerChoice, player)
