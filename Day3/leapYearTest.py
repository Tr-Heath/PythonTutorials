#Detirmine if a given year is a leap year or not.

year = int(input("Robin Williams: WHAT YEAR IS IT?!?! "))

def IsLeapYear(year):
    if(year % 400 == 0):
        return True
    elif (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
    

if(IsLeapYear(year)):
    print("It is a leap year.")
else:
    print("Not this year.")