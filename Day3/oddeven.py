#warm up exercise playing with conditionals
#Decipher if an integer is even or odd.

numTest = int(input("Give a number to test whether even or odd: "))

def printOddEvenIntTest(numTest):
    if(numTest % 2 == 0):
        print(f"{numTest} is an even number!")
    else:
        print(f"{numTest} is an odd number!")

printOddEvenIntTest(numTest)