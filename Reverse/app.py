input = raw_input("Enter a sentence that you would like to reverse: ")
output = ""

# Reverse string
for word in reversed(input):
    output += word

print output