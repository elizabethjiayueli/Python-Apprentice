from tkinter import messagebox, simpledialog, Tk
import sys
import random


window = Tk()
window.withdraw()

# 1. Change this line to give you a random number between 1 - 100.
random_num = random.randint(1, 101)

# 2. Print out the random variable that you made in step #1
print(random_num)
# 3. Code a for loop to run steps 4-10, 10 times
for i in range(10):

    # 4. Ask the user for a guess using a pop-up window, and save their response
    guess = simpledialog.askinteger("HIGH LOW GAME", "Enter a number from 1-100")
    # 5. If the guess is correct
        # 6. Win. Use 'sys.exit(0)' to end the program
    if guess == random_num:
        sys.exit(0)
    elif guess > random_num:
        messagebox.showinfo("HIGH LOW GAME", "It's too high")
    # 7. if the guess is high
        # 8. Tell them it's too high
    # 9. Else if the guess is low
        # 10. Tell them it's too low
    elif guess < random_num:
        messagebox.showinfo("HIGH LOW GAME", "It's too low")
    else:
        pass

#11. Outside of the loop, tell the user they lost
messagebox.showinfo("HIGH LOW GAME", "YOU LOST, TRY AGAIN")
window.mainloop()
