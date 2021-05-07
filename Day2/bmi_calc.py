#Calculate BMI given the necessary inputs.

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))


print(weight / height ** 2)
print(int(weight / height ** 2))