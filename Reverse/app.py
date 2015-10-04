input = input("Enter a sentence that you would like to reverse: ")
output = ""

# Reverse string and output it
for word in reversed(input):
    output += word

print output