from Start import *

# Perferences
speed = 5
turnDegrees = 30

# Define ins
instructions = "Press these buttons to move the turtle:\n\rW = go forward\n\rS = reverse\n\rA = rotate left\n\rD = rotate right\n\rH = repeat instructions\n\r"
print instructions

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

    #H repeat instructions
    if key == 104:
        print instructions


run(Program)
from End import *