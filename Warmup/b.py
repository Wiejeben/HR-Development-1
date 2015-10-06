# Define variables
valid = False

while not valid:
    # Get temperature in Kelvin
    celsius = input("Celsius: ")
    kelvin = celsius + 273.15

    if kelvin < 0:
        print "Your temperature is below absolute zero, please try again."
    else:
        valid = True
        print "\n\rResults:"
        print "Kelvin:", kelvin