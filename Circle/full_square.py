width = input("Enter the width of the square: ")
result = ""

for i in range(width):
    for j in range(width):
        result += "*"
    result += "\n"

print result