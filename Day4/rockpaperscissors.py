#Warm up exercise leveraging randomization functionality in python. 
import random, gameimages

#pass an int 0-2 and return image of choice
def choiceImage(comp):
    if int(comp) == 0:
        return gameimages.rock
    elif int(comp) == 1:
        return gameimages.paper
    else:
        return gameimages.scissors

print("Welcome to the game rock, paper scissors!")
choice = input("Please type your choice. '0' for rock, '1' for paper and '2' for scissors.")
compImage = choiceImage(random.randint(0, 2))
playerImage = choiceImage(choice)

print(f"You have chosen:")
print(playerImage)
print("Computer has:")
print(compImage)
