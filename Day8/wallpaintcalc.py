#warm up exercise
#Calculate how much paint is needed to cover a wall of a given height width
import math

COVERAGE = 375
height = 0
width = 0

def getPaintAmount(height, width):
    return math.ceil((height*width) / COVERAGE)

width = float(input("What is the width of the wall in feet? "))
height = float(input("What is the height of the wall in feet? "))

print(f"Total number of paint cans you should buy are {getPaintAmount(height, width)}")