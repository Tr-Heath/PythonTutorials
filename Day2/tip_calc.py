#build a tip calc
#Ask for the total bill, percentage to give and the number of ways to split the bill.
#Each person should pay round((bill / numPeople) * tipPercentage num,places)

#TODO: tip calculation should be a function, validate input.
print("Welcome to the tip calculator.")
total = float(input("What was the total bill? "))
tip = 1 + (int(input("What should the tip percentage be? ")) / 100)
numPeople = int(input("How many people are paying for the bill? "))
perPerson = (total / numPeople) * tip
formatPerPerson = "{:.2f}".format(perPerson,2)


print(f"The amount per person should be: ${formatPerPerson}")
