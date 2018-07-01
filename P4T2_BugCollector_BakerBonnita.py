# CTI-110
# BugCollector
# Bonnita Baker
# 6/30/2018


# This program will calculate a running total of the number
# of bugs collected during the seven day period.
# The program will ask for the number of bugs collected each day
# and will calculate the total number of bugs collected for the seven
# days.

def main():
# Initialize the accumulator
    total = 0

# Get the bugs collected for each day.
    for day in range (1, 8):
        print('Enter the bugs collected on day', day)
        bugs = int(input())
        total += bugs

# Display the total bugs
    print('You collected a total of', total, 'bugs.')




# Program start
main()
