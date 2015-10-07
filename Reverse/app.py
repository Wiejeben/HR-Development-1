input = raw_input("Enter a sentence that you would like to reverse: ")
result = ""
inputLength = len(input)

for i in range(inputLength):
    # Append specified character to results
    result += input[inputLength - (i + 1)]

print result