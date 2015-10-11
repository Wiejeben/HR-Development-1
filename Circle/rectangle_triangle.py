width = input("Enter the width of the rectangle triangle: ")
current_width = 0
result = ""

for _ in range(width):
    current_width += 1

    for _ in range(current_width):
        result += "*"

    result += "\n"

print result