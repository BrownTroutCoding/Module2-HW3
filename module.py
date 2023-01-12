import math

def printName(name):
    return "Hello Mr/Ms {name}...we've been waiting for you!"

def SF_house():
    length = int(input("Enter the length of your home in feet: "))
    width = int(input("Enter the width of your home in feet:"))
    area = length * width
    print("This is the total area of your home: ")
    print(area)
SF_house()

def circumference():
    radius = float(input("Enter the radius of the circle: "))
    return 2 * math.pi * radius
print(circumference())