number = input("Enter a absolute value: ")

# Best method
print "Lazy method:", abs(number)

# Ignore this
print "Wrong method:", str(number).strip('-')

# Manual ABS with times
if number < 0:
    times = number * -1
else:
    times = number

print "Times:", times


# Manual ABS with minus
if number < 0:
    minus = -number
else:
    minus = number

print "Minus:", minus