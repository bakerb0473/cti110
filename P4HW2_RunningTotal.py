# CTI-110
# P4HW2-RunningTotal
# Bonnita Baker
# 6/30/2018

# This program will ask the user to enter a series of numbers
# it will loop adding the numbers to a running total until
# the user enters a negative number, then the loop will exit


def main():
    total = 0
    print('Enter a negative number to exit.')

#Get the first number
    userNumber = float(input('Please enter the first number: '))

#Get the remaining numbers
    while userNumber > -1:
        total = total + userNumber
        userNumber = float(input('Please enter the next number: '))

#Display the sum
    print('The sum of all the numbers entered is: ', total)






# Start program
main()

                           
