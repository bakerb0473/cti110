# CTI-110
# P3H2 - Software Sales
# Bonnita Baker
# 6/24/2018

# This program will ask the user to enter the number of packages purchased
# it will display the amount of the discount
# and the total purchase cost with the discount applied

# If the quantity is less than 10 there is no discount
package = 99
quantity = float(input("How many packages are your ordering? "))
if quantity < 10:
    print("Total: $ ", package)
if quantity >= 10 and quantity <= 19:
    print("Total: $ ", (package * quantity) - (package * quantity) * .10)
if quantity >= 20 and quantity <= 49:
    print("Total: $ ", (package * quantity) - (package * quantity) * .20)
if quantity >= 50 and quantity <= 99:
    print("Total: $ ", (package * quantity) - (package * quantity) * .30)
if quantity >= 100:
    print("Total: $ ", (package * quantity) - (package * quantity) * .40)
    
    



