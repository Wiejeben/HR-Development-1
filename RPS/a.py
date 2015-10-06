import random

# Options
options = [
    "rock",
    "paper",
    "scissors",
]

valid = False

while not valid:

    # Ask for user input
    print "Choose rock, paper or scissors: "
    player_1 = raw_input("Player 1: ").lower()
    player_2 = raw_input("Player 2: ").lower()

    if not player_1 in options or not player_2 in options:
        print "Please both enter a valid option.\n\r"
    else:
        if player_1 == player_2:
            print "You both chose the same object, try again!\n\r"
        else:
            # Finish application
            valid = True

            print "\n\rResults:"
            if(
                player_1 == "rock" and player_2 == "scissors" or
                player_1 == "paper" and player_2 == "rock" or
                player_1 == "scissors" and player_2 == "paper"
            ):
                print "Player 1 wins with", player_1
                print "Player 2 loses with", player_2
            else:
                print "Player 1 loses with", player_1
                print "Player 2 wins with", player_2