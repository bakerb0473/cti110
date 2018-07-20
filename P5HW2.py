# CTI-110
# High-Low.py - number guessing game
# Bonnita Baker
# 7/8/2018


# use the random module
import random

# set constant values for minimum, maximum
MIN = 1
MAX = 100

def main():
    # use a variable to control the loop
    again = 'y'

# The player will guess a number 1 to 100
# The number will be called secretNumber
def play_game():
    from random import randint
    secretNumber = randint(1,100)
    guess = -1
    


# If the player guesses too high
    while guess != secretNumber:
        guess = int(input('Guess a number: '))
        if guess > secretNumber:
            print('Too high, try again.')

# If the player guesses too low
        elif guess < secretNumber:
            print('Too low, try again.')

# If the player guesses correctly
        if guess == secretNumber:
            print('Congratulations! Just right!')

# until the user is finished repeat
    while again == 'y' or again == 'Y':
        # player will be able to continue to guess
        print('Guess again? ')






# call the main function
main()







# Program start
main()
