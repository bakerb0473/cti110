# CTI-110
# high-low.py -- number guessing game 
# Bonnita Baker
# 7/8/2018


import random

def main():
    name = input('Hello, what is your name? ')
    secretNumber = random.randint(1,100)
    print('Hi', name, "I'm thinking of a number between 1 and 100.")
    again = input('Wanna play again? ')
    guess = -1


def play_game():
    from random import randint
    secretNumber = randint(1,100)
    


while guess != secretNumber:
    guess = int(input('Enter a guess: '))
    if guess < number:
        print('Too low, try again.')
    elif guess > number:
        print('Too high, try again.')
    else:
        break


if guess == secretNumber:
    print('Congratulations!', name, 'You rock!')
else:
    print('Awww. Better luck next time. The correct number is:', number)






# Program start
main()
        
    
        
    





 



            
