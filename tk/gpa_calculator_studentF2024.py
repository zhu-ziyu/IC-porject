from tkinter import *
from tkinter.font import Font
import random


def calculate_gpa():
    n1=int(num1_var.get())
    n2=int(num2_var.get())
    n3=int(num3_var.get())
    n4=int(num4_var.get())
    avg = (n1 + n2 + n3 + n4) / 4
    tolal_var.set(avg)  # 调用 set()，把结果写入 StringVar

#MAIN
#HOlding frames
#########
root = Tk()
mainframe = Frame(root)

small_font = Font(family="Arial", size=20)

#Widgets
#########

instruction_label = Label(mainframe, text="Enter your 4 course grades")

num1_var = StringVar()
num1_entry = Entry(mainframe, width=5, font=small_font, textvariable=num1_var)

num2_var = StringVar()
num2_entry = Entry(mainframe, width=5, font=small_font, textvariable=num2_var)

num3_var = StringVar()
num3_entry = Entry(mainframe, width=5, font=small_font, textvariable=num3_var)

num4_var = StringVar()
num4_entry = Entry(mainframe, width=5, font=small_font, textvariable=num4_var)

gpa_button = Button(mainframe, text="FIND GPA", command=calculate_gpa)

tolal_var = StringVar()
tolal_label=Label(mainframe,textvariable=tolal_var)

#GRID THE WIDGETS
###########

mainframe.grid(padx=100, pady=100)
instruction_label.grid(row=1, column=1, columnspan=3)
num1_entry.grid(row=2, column=1)
num2_entry.grid(row=2, column=2)
num3_entry.grid(row=2, column=3)
num4_entry.grid(row=2, column=4)

gpa_button.grid(row=3, column=1, columnspan=4, ipadx=80, pady=30)
tolal_label.grid(row=4, column=1)

root.mainloop()