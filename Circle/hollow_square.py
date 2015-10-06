width = input("Enter the width of the square: ")
result = ""

for i in range(width):

    # top and bottom
    if i == 0 or i == width-1:
        for j in range(width):
            result += "*"
    else:
        # body
        for j in range(width):
            if j == 0 or j == width-1:
                result += "*"
            else:
                result += " "

    result += "\n"

print result