#CTI-110
#P3T1-Areas of Rectangles
#Bonnita Baker
#06/19/2018
#

#This program will calculate the area of 2 rectangles and will tell the user
#which rectangle has the greatest area or if the area of the two are the same

#Get the dimensions of Rectangle 1
L1 = int(input('Enter the length of Rectangle 1:'))
W1 = int(input('Enter the width of Rectangle 1:'))

#Get the dimensions of Rectangle 2
L2 = int(input('Enter the length of Rectangle 2:'))
W2 = int(input('Enter the width of Rectangle 2:'))

#Calculate the areas of the rectangles
A1 = L1 * W1
A2 = L2 * W2

#Determine which has the greatest area
if A1 > A2:
    print('Rectangle 1 has the greatest area.')
elif A2 > A1:
    print('Rectangle 2 has the greatest area.')
else:
    print('Both have the same area.')
    
        
