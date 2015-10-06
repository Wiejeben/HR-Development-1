space = input("Enter the width of the isosceles triangle: ")
result = ""

for row in range(0, space):

    # Get width of the triangle
    width = space - 1

    for column in range(0, space + width):

        # Check if current column position is not within the triangle
        if column - width + row < 0 or column - width - row > 0:
            result += " "
        else:
            result += "*"
    result += "\n"

print result