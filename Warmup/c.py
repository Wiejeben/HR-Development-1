import math

number = float(input("Enter a absolute value: "))

print("Lazy method: " + str(math.fabs(number)))

print("Wrong method: " + str(number).strip('-'))