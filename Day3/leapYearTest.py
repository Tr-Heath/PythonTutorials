#Detirmine if a given year is a leap year or not.

year = int(input("Robin Williams: WHAT YEAR IS IT?!?! "))

def notifyItIsLeapYear():
    print("It is a leap year!")

if(year % 400 == 0):
    notifyItIsLeapYear()
elif (year % 4 == 0 and year % 100 != 0):
    notifyItIsLeapYear()
else:
    print("Not a leap year.")