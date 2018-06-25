# CTI-110
# P3HW1 - Age Classifier
# Bonnita Baker
# 6/24/2018

# This program will ask the user to enter their age
# This program will determine if the person is an infant, child, teenager
# or adult


# Get the person's age
age = float(input("How old are you? "))

# If the age is less than or equal to 1 then the person is an infant
if age <= 1:
    print("You are an infant.")

# If the age is greater than 1 year but less than 13 years
# the person is a child
if age > 1 and age < 13:
    print("You are a child.")

# If the age is 13 to 19 the person is a teenager
if age >= 13 and age < 20:
    print("You are a teenager.")


# If the age is 20 or older the person is an adult
if age >= 20:
    print("You are an adult.")
    
        


    
      
      

      

        
      
