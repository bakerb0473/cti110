# CTI-110
# P4LAB-Snowflake
# Bonnita Baker
# 7/1/2018


# Create a turtle graphics program that draws a shape using a nested loop

def  main():
    import turtle
    turtle.forward(0)
    
    import random
    elsa = turtle.Turtle()

    turtle.Screen().bgcolor('lavender')
    
    elsa.forward(90)
    elsa.left(45)
    
    def branch():
        for i in range(3):
            for i in range(3):
                elsa.forward(30)
                elsa.backward(30)
                elsa.right(45)
            elsa.left(90)
            elsa.backward(30)
            elsa.left(45)
        elsa.right(90)
        elsa.forward(90)

    for i in range(8):
        branch()
        elsa.left(45)
            







# Program start
main()
