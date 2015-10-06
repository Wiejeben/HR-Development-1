password = raw_input("Please enter a password: ")
length = len(password)

# Initial strength
strength = 0

# Check for length
if(length > 6):
    strength += length-6

# Check password per character
for x in password:

    # Check for numbers
    if(x.isdigit()):
        strength += 1

    # Check for capitals
    elif(x.isupper()):
        strength += 1

    # Check for special characters
    elif(not x.isalpha()):
        strength += 1

print "Strength: ", strength

# Get results
result = "Strong"

# Overwrite the result if the strength is low
if strength < 8:
    result = "Weak"

elif strength < 20:
    result = "Medium"

print "Password strength:", result