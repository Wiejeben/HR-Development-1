password = input("Please enter a password: ")
strength = 0
length = len(password)

# Check for length
if(length >= 5):
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
if strength < 8:
    result = "Weak"

elif strength < 20:
    result = "Medium"

else:
    result = "Strong"

print "Password strength:", result