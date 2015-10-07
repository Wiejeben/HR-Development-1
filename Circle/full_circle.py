from math import sqrt

diameter = input("Enter the diameter of the full circle: ")
radius = diameter / 2
result = ""

for y in range(diameter):

    for x in range(diameter):

        # If cursor position is within the radius via formula of Pythagoras
        if sqrt(pow(x - radius, 2) + pow(y - radius, 2)) < radius:
            result += "*"
        else:
            result += " "

    result += "\n"

print result