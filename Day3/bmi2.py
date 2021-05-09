#Enhance the BMI calculator from Day 2.
#Give an interperatation of the value given.

def categorizeBMIValue(bmi):
    if bmi < 18.5:
        print(f"A BMI of {bmi} is underweight.")
    elif bmi < 25:
        print(f"A BMI of {bmi} is a normal weight.")
    elif bmi < 30:
        print(f"A BMI of {bmi} is a overweight.")
    elif bmi < 35:
        print(f"A BMI of {bmi} is a obese.")
    else:
        print(f"A BMI of {bmi} is a clinically obese.")

def calcBMI(height, weight):
    return round(weight / height ** 2, 1)

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

categorizeBMIValue(calcBMI(height, weight))