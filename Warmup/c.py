import math

number = input("Enter a absolute value: ")

print "Lazy method: ", abs(number)

print "Wrong method: ", str(number).strip('-')

if(number < 0):
    number = number * -1

print "With an IF: ", number