from Start import *

# Perferences
speed = 5
turnDegrees = 30

# Define ins
print "Press these buttons to move the turtle:\n\rW = go forward\n\rS = reverse\n\rA = rotate left\n\rD = rotate right\n\r"

def Program():
    key = get()

    #W go forward
    if key == 119:
        forward(speed)

    #S reverse
    if key == 115:
        turn(180)
        forward(speed)

    #A rotate left
    if key == 97:
        turn(-turnDegrees)

    #D rotate right
    if key == 100:
        turn(turnDegrees)


run(Program)
from End import *