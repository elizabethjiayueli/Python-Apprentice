"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules

# Create a window object
from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups
# Hide the window, hint: use the withdraw method

# Ask the user for the first number   
a1 = simpledialog.askinteger("Adding Calculator", "Insert first number")
# Ask the user for the second number
a2 = simpledialog.askinteger("Adding Calculator", "Insert second number")
# Display the sum of the two numbers 
a = a1 + a2

messagebox.showinfo("Your Answer:", a)
# Keep the window open

