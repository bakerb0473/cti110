#CTI-110
#P2HW2-TipTaxTotal
#Bonnita Baker
#6/15/2018
#

#This program calculates the total cost of a meal purchased at a restaurant

#Get the cost for the food
foodCost = float(input('What was the cost of your food: $'))


#Get the sales tax, tax is 7 percent
print('Tax due: $', (foodCost * 0.07))


#Display the tip amount rounded to the nearest dollar, the tip is 18 percent
print('Please tip your Server: $', int(foodCost * 0.18))

                                        

