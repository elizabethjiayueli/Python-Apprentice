
"""
Hotel Management System
1. Functions needed:
    1a. Be able to check in or check out
    1b. recieve price
    1c. choose room
    1d. how many guests
5. Should use lists, tuples, dictionaries
6. All functionality in functions
"""
from tkinter import messagebox, simpledialog,Tk
window = Tk()
window.withdraw()
db = {}

def in_or_out(db):
    rooms = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    while True:
        ask = simpledialog.askstring("HOTEL MANAGEMENT", "What is your name?")
        check = simpledialog.askstring("HOTEL MANAGEMENT", "Would you like to check in or check out?")
        if check == "check in" or check == "in":
            peeps_num = simpledialog.askinteger("HOTEL MANAGEMENT", "How many people are you traveling with?")
            if int(peeps_num) <= 6:
                room = simpledialog.askinteger("Which room would you like?", rooms)
                rooms.remove(room)
                days = simpledialog.askinteger("HOTEL MANAGEMENT", "How many days are you going to stay?")
                price = 200*days + peeps_num
            elif int(peeps_num) >= 7:
                num_rooms = (simpledialog.askinteger("HOTEL MANAGEMENT", "Please choose 2 or more rooms. Enter the number of rooms you would like."))
                for i in range(num_rooms):
                    room = simpledialog.askstring("Which rooms would you like?", rooms)
                    rooms.remove(room)
                days = simpledialog.askinteger("HOTEL MANAGEMENT", "How many days are you going to stay?")
                price = 200*days + peeps_num * num_rooms
            db[ask] = room
            messagebox.showinfo("Your price is $", price)
        elif check == "check out" or check == "out":
            if ask in db:
                value = db.pop(ask) 
                messagebox.showinfo("HOTEL MANAGEMENT", "I hope you enjoyed your stay!")
            else:
                messagebox.showerror("error")
        else:
            messagebox.showwarning("invalid response", "please try again")
        messagebox.showinfo("HOTEL MANAGEMENT", db)
in_or_out(db)