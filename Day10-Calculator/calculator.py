#Create a calculator that can perform the standard operations MDAS.
from calc_art import logo
result = [0.0, "n"]
operators = ['+', '-', '*', '/']

def calculate(a, b, opp):
    print(opp)
    if opp == "+":
        return a + b
    elif opp == "-":
        return a - b
    elif opp == "*":
        return a * b
    elif opp == "/":
        if b != 0:
            return a / b
        else:
            return "NaN" #return string indicating result is not a number

def getUserInput(result):
    if(result[1].lower() == "n"):
        result[0] = float(input("What is the first operand? "))
    opp = input("Desired operator? ('+', '-', '*', '/') ")
    if opp not in operators:
        opp = input("Invalid operator, please try again: ")
    b = float(input("And the second operand? "))
    c = calculate(result[0], b, opp)
    print(f"{result[0]} {opp} {b} = {c}")
    if isinstance(c, float):
        result[0] = c
        result[1] = input(f"Type 'y' to continue calculating with {result[0]} as the first operand or 'n' to start fresh. 'q' to quit Calculator. ")
    else:
        print('Invalid input resulted in divide by zero.')
        result[1] = "n"
    return result

print(f"{logo}")
while result[1] != "q":
    result = getUserInput(result)


