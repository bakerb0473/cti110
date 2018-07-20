# CTI-110
# High_Low
# Bonnita Baker
# 7/5/2018

# This program will generate a random number in the range of 1 to 100
# The user will be asked to guess the secret number
# If the number guessed is too high, the program will tell the user
# Too high, try again.
# If the users guess is lower than the secret number, the program will tell
# the user Too low, try again.
# If the user guesses correctly, the program will congratulate the user


# main function
def main():
    guess = 0
    secretNumber = random.radint(1,100)
    # To roll again?
    again = input('Play again? (y = yes): ')
    
# The user will guess a number 1 to 100 we'll call this number 'secretNumber'
    def play_game():
        from random import randint
        secretNumber = randint(1, 100)
        guess = -1
        
    # if the guess is too high
    while guess != secretNumber: 
        guess = int(input ("Guess a number: "))
        if guess > secretNumber:
            print("Too high, try again.")
            
    # if the guess is too low
        elif guess < secretNumber:
                print("Too low, try again.")
                
    # if the guess is correct
        if guess == secretNumber:
            print("Congratulations! Just right!!!")





# program start
main()



