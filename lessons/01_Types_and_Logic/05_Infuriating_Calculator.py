"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups
# Hide the window, hint: use the withdraw method

# Ask the user for the first number   
a1 = simpledialog.askinteger("Calculator", "Insert first number")
# Ask the user for the second number
a2 = simpledialog.askinteger("Calculator", "Insert second number")
# Create a window object
a3 = simpledialog.askstring("Calculator", """Insert the name of the operation you are performing: 1 for Addition, 2 for Subtraction, 
                                  3 for Multiplication, 4 for Division""")
if a3 == "1":
   a = a1 + a2
elif a3 == "2":
   a = a1 - a2
elif a3 == "4":
   a = a1/a2
elif a3 == "3":
   a = a1*a2
else:
   a = a1*a2
messagebox.showinfo("Your Answer", a)
# Hide the window, hint: use the withdraw method

# Ask the user for the first number   

# Ask the user for the second number

# Ask the user for the math operation

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open
