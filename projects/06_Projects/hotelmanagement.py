
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
from tkinter import messagebox, simpledialog


def in_or_out():
    check = simpledialog.askstring("HOTEL MANAGEMENT", "Would you like to check in or check out?")
    if check == "check in":
        simpledialog.askstring("HOTEL MANAGEMENT"), ""