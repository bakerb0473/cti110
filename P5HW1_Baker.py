# Test Average and Grade
# 7/5/2018
# CTI-110 P5HW1 - Test Average and Grade
# BonnitaBaker
#.


# Write a program that asks the user to enter five test grades. The program
# should display a letter grade for each score and the average test score.
# Write the following functions in the program:

# main() - this function will control the main flow of the program. It will
# call the next two functions to do most of the work
# It should also hold the input() commands to allow the user to type in grades.

# calc_average - This function should accept five test scores as arguments
# and return the average of the scores.

# determine_grade - This function should accept five test scores as arguments
# and return the average of the scores.

#   Score       Letter Grade
#   90 - 100        A
#   80 - 89         B
#   70 - 79         C
#   60 - 69         D
#   Below - 60      F


# main function
def main():
    herescores = input("Enter five test scores seperated by commas:")
    

# Determin grade
def determine_grade(grades):
    for num in grades:
        if int(num) >= 90 and int(num) <= 100:
            print("A")
        elif int(num) >=80 and int(num) <= 89:
            print("B")
        elif int(num) >=70 and int(num) <= 79:
            print("C")
        elif int(num) >=60 and int(num) <= 69:
            print("D")
        else:
            print("F")

# Calculate average
def calc_average(grades):
    total = 0
    for num in grades:
        total += int(num)
    average = total / 5
    print(average)


#def show_letters(values):
main()
