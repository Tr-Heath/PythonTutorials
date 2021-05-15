#Little Python script to generate random passwords.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

allchars = []
#0 letters, 1:symbols, 2:numbers
variationtracker = [0, 0, 0]
variationdesired = [0, 0, 0]

allchars.append(letters)
allchars.append(numbers)
allchars.append(symbols)


print(allchars)

print("Welcome to the PyPassword Generator!")
variationdesired[0] = int(input("How many letters would you like in your password?\n")) 
variationdesired[1] = int(input(f"How many symbols would you like?\n"))
variationdesired[2] = int(input(f"How many numbers would you like?\n"))
nr_total = sum(variationdesired)
passwordlength = 0
added_letters = 0
added_symbols = 0
added_numbers = 0

password = ''

while nr_total > passwordlength:
    chartype = random.randint(0,2)
    if variationtracker[chartype] < variationdesired[chartype]:
        print(variationdesired)
        print(variationtracker)
        print(chartype)
        variationtracker[chartype] += 1
        charindex = random.randint(0,len(allchars[chartype])-1)
        password += allchars[chartype][charindex]
        passwordlength += 1

print(password)
print(variationtracker)
