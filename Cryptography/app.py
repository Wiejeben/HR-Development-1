message = input("Enter a message: ")
offset = int(input("Encryption offset (number): "))
result = ""

for char in message:

    if char.isalpha():

        number = ord(char) + offset

        if char.isupper():
            # Uppercase
            if number > ord("Z"):
                number = number - 26

            elif (number < ord("A")):
                number = number + 26

        else:
            # Lowercase
            if number > ord("z"):
                number = number - 26

            elif (number < ord("a")):
                number = number + 26

        char = chr(number)
    result += char

print result