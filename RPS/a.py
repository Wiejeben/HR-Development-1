import random

# Options
options = [
    "rock",
    "paper",
    "scissors"
]

valid = False

while(not valid):
    print("Choose rock, paper or scissors: ")
    player_1 = input("Player 1: ").lower()
    player_2 = input("Player 2: ").lower()

    if(not player_1 in options or not player_2 in options):
        print("Please both enter a valid option.\n\r")
    else:
        print("\n\rResults:\n\rPlayer 1: " + player_1.capitalize() + "\n\r" + "Player 2: " + player_2.capitalize())

        if(player_1 == player_2):
            print("You both chose the same object, try again!\n\r")
        else:
            valid = True

            if(player_1 == "rock" and player_2 == "scissors" or
               player_1 == "paper" and player_2 == "rock" or
               player_1 == "scissors" and player_2 == "paper"):
                print("\n\rPlayer 1 wins")
            else:
                print("\n\rPlayer 2 wins")