import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()


amountOfLines = len(lines) 
indexMax = len(lines[0])

def slope(xIncrement, yIncrement):
    amountOfTrees = 0
    verticality = 0
    index = 0
    while verticality < amountOfLines:
        if lines[verticality][index] == "#":
            amountOfTrees += 1
        verticality += yIncrement
        index += xIncrement
        if index >= indexMax:
            index =  index % indexMax

    return amountOfTrees




print("Right 1, down 1:", slope(1, 1))
print("(part 1) Right 3, down 1:", slope(3, 1))
print("Right 5, down 1:", slope(5, 1))
print("Right 7, down 1:", slope(7, 1))
print("Right 1, down 2:", slope(1, 2))

print("All multiplied together:", slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))