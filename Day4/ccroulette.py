#Quick version of credit card roulette as a coding exercise utilizing lists and random numbers
import random

print("Who will be risking their credit card to pay for the bill?")
names = input("Separate each name with a comma: ").split(',')
print(names[random.randint(0,len(names))].strip())