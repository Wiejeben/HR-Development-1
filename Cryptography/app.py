message = raw_input("Enter a message: ")
offset = input("Encryption offset (number): ")
result = ""
offset %= 26

for char in message:

    if char.isalpha():

        # Apply offset
        number = ord(char) + offset

        if char.isupper():
            # Uppercase
            if number < ord("A"):
                number = number + 26

            elif number > ord("Z"):
                number = number - 26

        else:
            # Lowercase
            if number < ord("a"):
                number = number + 26

            elif number > ord("z"):
                number = number - 26

        char = chr(number)
    result += char

print result