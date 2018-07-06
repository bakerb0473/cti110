# CTI-110
# P5T1_Kilometer-Converter
# Bonnita Baker
# 7/5/2018



# This program wil ask the user to enter a distance in kilometers
# then covert that distance to miles

# The conversion formula
#   Miles = Kilometers * 0.6214

# 2 functions will be created for this program:
#   A main() function, and
#   A show_miles() function that takes km as a parameter,
#       converts to miles,
#       and prints the answer



CONVERSION_FACTOR = 0.6214  # This is a global constant

# The main function gets a distance in km and calls
# the show_miles function to convert it

def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles
    show_miles(kilometers)

# The show miles function converts the parameter km from
# kilometers to miles and displays the result

def show_miles(km):
    # Calculate miles.
    miles = km * CONVERSION_FACTOR

    # Display the miles
    print(km, 'kilometers equals', miles, 'miles.')


# Program start
main()





