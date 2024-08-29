"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

colors = [ 'red', 'yellow', 'black', 'orange']    # define a list of colors

for i in list(colors):                            # loop through the colors
    ... # Your code here
    tina.color(i)
    tina.forward(50)
    tina.left(90)


turtle.done()