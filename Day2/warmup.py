#Working with Data Types and basic math operations
#lets create a tip calculator

#Let's warm up with inputs and operations

#Quick refresher, apparently Python doesn't hoist like JavaScript does
def askForInput():
    return input("Type a two digit number: ")

#Future enhancement, check typeof input
def checkNumDigits(stringcheck):
    if(len(stringcheck) == 2) :
        print(calc(stringcheck))
    else :
        print("Please give exactly two digits.")
        checkNumDigits(askForInput())

def calc(userInput):
    first = int(userInput[0])
    second = int(userInput[1])
    return first + second

checkNumDigits(askForInput())
