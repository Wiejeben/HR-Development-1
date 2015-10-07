height = input("Enter the height of the piramid: ")
result = ""
stars = 1
whitespace = height

for i in range(height):

    whitespace -= 1

    for x in range(whitespace):
        result += " "

    for x in range(stars):
        result += "*"

    stars += 2
    result += "\n"

print result