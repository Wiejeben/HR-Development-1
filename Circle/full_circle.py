import math

diameter = input("Enter the diameter of the full circle: ")
radius = diameter / 2
result = ""

for i in range(diameter):

    for j in range(diameter):

        # If cursor position is within the circle via formula of Pythagoras
        if math.sqrt(pow(i - radius, 2) + pow(j - radius, 2)) < radius:
            result += "*"
        else:
            result += " "

    result += "\n"

print result