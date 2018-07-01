# CTI-110
# P4HW1-DistanceTraveled
# Bonnita Baker
# 6/30/2018


# Write a program that asks the user two questions:
# Question 1: The speed of a vehicle
# Question 2: The number of hours it has traveled
# The program will then display the distance that the vehicle has
# traveled for each hour of that time period.
# The output should be displayed in table format

def main():
# The distance a vehicle travels can be calculated using this formula

# distance = speed * time

# The user will enter the speed    
    vehicleSpeed = float(input('What is the speed of the vehicle?: '))
    print()
# The user will enter the number of hours it has traveled
    timeTraveled = int(input('How many hours it has traveled?: '))
    print()
# Calculate the distance the vehicle has traveled for each hour
    print('Hour','\t','Distance Traveled')
    for currentHour in range (1, timeTraveled + 1):
        distanceTraveled = vehicleSpeed * currentHour
        print(currentHour,'\t','\t',distanceTraveled)
        


                        


# Program start
main()
