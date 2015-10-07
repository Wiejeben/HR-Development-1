height = input("Enter the height of the piramid: ")
result = ""
stars = 1
whitespace = height

for _ in range(height):

    whitespace -= 1

    for _ in range(whitespace):
        result += " "

    for _ in range(stars):
        result += "*"

    stars += 2
    result += "\n"

print result