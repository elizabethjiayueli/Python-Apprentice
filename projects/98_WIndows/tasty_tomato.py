from tkinter import messagebox, simpledialog
import tkinter as tk

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
color = simpledialog.askstring("TASTY_TOMATO", "which color would u like ur tomato to be? Red, brown, yellow, purple, pink, or orange?")
stem = simpledialog.askstring("TASTY_TOMATO", "which color would u like ur tomato stem to be? green, brown, pink, cyan, or yellowish green?")
# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if stem == "green":
    if color == "red":
        canvas.create_oval(74, 200, 400, 450, fill="red", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    elif color == "orange":
        canvas.create_oval(74, 200, 400, 450, fill="orange", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="orange", outline="")
    elif color == "yellow":
        canvas.create_oval(74, 200, 400, 450, fill="yellow", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")
    elif color == "purple":
        canvas.create_oval(74, 200, 400, 450, fill="purple", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="purple", outline="")
    elif color == "pink":
        canvas.create_oval(74, 200, 400, 450, fill="pink", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="pink", outline="")
    elif color == "brown":
        canvas.create_oval(74, 200, 400, 450, fill="brown", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="brown", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="teal", outline="")
elif stem == "brown":
    if color == "red":
        canvas.create_oval(74, 200, 400, 450, fill="red", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    elif color == "orange":
        canvas.create_oval(74, 200, 400, 450, fill="orange", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="orange", outline="")
    elif color == "yellow":
        canvas.create_oval(74, 200, 400, 450, fill="yellow", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")
    elif color == "purple":
        canvas.create_oval(74, 200, 400, 450, fill="purple", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="purple", outline="")
    elif color == "pink":
        canvas.create_oval(200, 200, 525, 450, fill="pink", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="pink", outline="")
    elif color == "brown":
        canvas.create_oval(74, 200, 400, 450, fill="brown", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="brown", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="purple", outline="")
elif stem == "yellowish green":
    if color == "red":
        canvas.create_oval(74, 200, 400, 450, fill="red", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    elif color == "orange":
        canvas.create_oval(74, 200, 400, 450, fill="orange", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="orange", outline="")
    elif color == "yellow":
        canvas.create_oval(74, 200, 400, 450, fill="yellow", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")
    elif color == "purple":
        canvas.create_oval(74, 200, 400, 450, fill="purple", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="purple", outline="")
    elif color == "pink":
        canvas.create_oval(74, 200, 400, 450, fill="pink", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="pink", outline="")
    elif color == "brown":
        canvas.create_oval(74, 200, 400, 450, fill="brown", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="brown", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="purple", outline="")
elif stem == "cyan":
    if color == "red":
        canvas.create_oval(74, 200, 400, 450, fill="red", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    elif color == "orange":
        canvas.create_oval(74, 200, 400, 450, fill="orange", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="orange", outline="")
    elif color == "yellow":
        canvas.create_oval(74, 200, 400, 450, fill="yellow", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")
    elif color == "purple":
        canvas.create_oval(74, 200, 400, 450, fill="purple", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="purple", outline="")
    elif color == "pink":
        canvas.create_oval(74, 200, 400, 450, fill="pink", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="pink", outline="")
    elif color == "brown":
        canvas.create_oval(74, 200, 400, 450, fill="brown", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="brown", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="cyan", outline="")
elif stem == "pink":
    if color == "red":
        canvas.create_oval(74, 200, 400, 450, fill="red", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    elif color == "orange":
        canvas.create_oval(74, 200, 400, 450, fill="orange", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="orange", outline="")
    elif color == "yellow":
        canvas.create_oval(74, 200, 400, 450, fill="yellow", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")
    elif color == "purple":
        canvas.create_oval(74, 200, 400, 450, fill="purple", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="purple", outline="")
    elif color == "pink":
        canvas.create_oval(74, 200, 400, 450, fill="pink", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="pink", outline="")
    elif color == "brown":
        canvas.create_oval(74, 200, 400, 450, fill="brown", outline="")
        canvas.create_oval(200, 200, 525, 450, fill="brown", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="pink", outline="")

root.mainloop()
