import random

# Scissors cut Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitate Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# Rock crushes Scissors

# Options
options = [
    "rock",
    "paper",
    "scissors",
    "lizard",
    "spock"
]

valid = False

while(not valid):
    print("Choose rock, paper, scissors, lizard or spock: ")
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

            if(
               player_1 == "rock" and player_2 == "scissors" or
               player_1 == "rock" and player_2 == "lizard" or

               player_1 == "paper" and player_2 == "rock" or
               player_1 == "paper" and player_2 == "lizard" or

               player_1 == "scissors" and player_2 == "paper" or
               player_1 == "scissors" and player_2 == "lizard" or

               player_1 == "spock" and player_2 == "rock" or
               player_1 == "spock" and player_2 == "scissors" or

               player_1 == "lizard" and player_2 == "spock" or
               player_1 == "lizard" and player_2 == "paper"
            ):
                print("\n\rPlayer 1 wins")
            else:
                print("\n\rPlayer 2 wins")