# Create a GUI program that simulates rolling a six-sided die.
# The program will have a button for rolling a die
# and a label for the result (a number from 1 to 6).

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import random


def result():
    x = random.randint(1,6)
    return x

def label_name():
    label.config(text=result())

root = tk.Tk()

label = tk.Label(root, text='', width=10, height=2, font='Times 12')
label.pack()

frame = tk.Frame(root, relief='raised', borderwidth=2)
frame.pack(side=tk.BOTTOM)

button = tk.Button(frame, text='Click',width=8, height=4,
    bg='#d694af', fg='#ebe4e7', font='Times 12 bold', command=label_name)
button.pack(side=tk.TOP)

root.mainloop()
