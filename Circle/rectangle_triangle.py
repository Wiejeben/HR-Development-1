width = input("How many stars wide would like your triangle to be: ")
current_width = 1
result = ""

for i in range(width):

    for j in range(current_width):
        result += "*"
    result += "\n"
    current_width += 1

print result