import math

diameter = input("Enter the diameter of the full circle: ")
radius = diameter / 2
result = ""

for i in range(diameter):

    # Calculate left half
    row = (i - radius) * (i - radius)

    for j in range(diameter):

        # Calculate right half
        column = (j - (radius)) * (j - (radius))

        # If cursor position is within the circle
        if math.sqrt(row + column) < radius:
            result += "*"
        else:
            result += " "

    result += "\n"

print result