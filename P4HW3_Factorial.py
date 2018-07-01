# CTI-110
# P4HW3-Factorial
# Bonnita Baker
# 6/30/2018


# Write a program that asks the user for a nonegative integer
# and then uses a loop to calculate the factorial of that number
# Display the factorial

def main():
    userInteger = int(input('Please enter a number: '))
    while userInteger < 1:
        userInteger = int(input('Please enter a positive number: '))

    factorial = 1

    for currentNumber in range (1, userInteger + 1):
        factorial *= currentNumber

    print('The factorial of', userInteger, 'is', factorial)







# Program start
main()
        
