"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error

t=turtle.Turtle()

def circle():
    t.circle(50, steps=50)

def square():
    for i in range(4):
        t.forward(50+0*i)
        t.right(90+0*i)


def triangle():
    for i in range(3):
        t.forward(50+0*i)
        t.right(120+0*i)

command = input("Circle, square, or triangle? ALL LOWERCASE!")
if command == "circle":
    circle()
elif command == "triangle":
    triangle()
elif command == "square":
    square()
else:
    t.write("ERROR")
# TODO)
#   1. Create a turtle.
#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
#   3. Ask the user for the for a shape to draw.
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
pass