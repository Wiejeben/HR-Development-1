# convert C to F with 2 decimals
f = float(input("Fahrenheit: "))
c = "{0:.2f}".format((f - 32) * 5 / 9)

# Show results
print("\n\rResults:")
print("Celsius: " + c)