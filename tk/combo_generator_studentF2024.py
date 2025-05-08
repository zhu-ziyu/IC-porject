from tkinter import *
from tkinter.font import Font
import random

def generate_random_combination():
    num1_var.set(random.randint(1,60))
    num2_var.set(random.randint(1,60))
    num3_var.set(random.randint(1,60))



#MAIN
#Holding frames
#########
root = Tk()
mainframe = Frame(root)

arial_font = Font(family="Arial", size=50)
mainframe.pack(padx=20, pady=20)   # <-- 放到 root 上，否则永远不显示


#Widgets
#########

num1_var = StringVar()
num1_label = Label(mainframe, font=arial_font, textvariable=num1_var)

num2_var = StringVar()
num2_label = Label(mainframe, font=arial_font, textvariable=num2_var)

num3_var = StringVar()
num3_label = Label(mainframe, font=arial_font, textvariable=num3_var)

random_button = Button(mainframe, text="NEW COMBO", command=generate_random_combination)

#GRID THE WIDGETS
###########
num1_label.grid(row=0, column=0)
num2_label.grid(row=0, column=1)
num3_label.grid(row=0, column=2)
random_button.grid(row=1, column=0)

root.mainloop()
