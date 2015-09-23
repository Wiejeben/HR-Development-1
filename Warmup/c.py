number = input("Enter a absolute value: ")

print "Lazy method: ", abs(number)

print "Wrong method: ", str(number).strip('-')

# Manually ABS with times
if number < 0:
    times = number * -1
else:
    times = number

print "Times: ", times


# Manually ABS with minus
if number < 0:
    minus = -number
else:
    minus = number

print "Minus: ", minus