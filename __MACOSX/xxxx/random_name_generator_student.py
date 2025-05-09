from tkinter import *
from tkinter.font import Font
import random


def get_names(filename):
    global all_names

    all_names = []

    fileIn = open(filename, encoding='utf-8', errors='replace')

    for line in fileIn:
        all_names.append(line.strip())

    return all_names


def generate_names():
    global all_names, name_var
    new_names = random.sample(all_names, 10)
    name_var.set(new_names)


# MAIN
global all_names
get_names("random_names.txt")

root = Tk()
root.config(bg="#293d3d")
mainframe = Frame(root, bg="#293d3d")

sunday_font = Font(family="Sunday", size=20)

title = Label(mainframe, text="Random Names", bg="#293d3d", fg="#ffffff", font=sunday_font)

# create the Listbox widget

name_var = StringVar(value=[])
name_listbox = Listbox(
    mainframe,
    listvariable=name_var,
    selectmode=SINGLE,
    width=30,
    height=10,
    font=sunday_font
)

random_button = Button(
    mainframe,
    text="Randomize",
    highlightbackground="#669999",
    font=sunday_font,
    command=generate_names
)

# Grid the widgets
mainframe.grid(padx=100, pady=100)
title.grid(row=0, column=1, pady=10)
name_listbox.grid(row=1, column=1, pady=20)
random_button.grid(row=2, column=1, sticky=EW, ipady=10)

root.mainloop()
