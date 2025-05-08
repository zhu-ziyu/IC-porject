from tkinter import *
import random

from sympy.physics.units import volume


def convert_number():
    cm_value = float(cm_var.get())
    target = unit_convert_var.get()
    if target == "mm":
        final = cm_value * 10
    elif target == "cm":
        final = cm_value
    elif target == "m":
        final = cm_value / 100
    elif target == "km":
        final = cm_value / 100000
    else:
        num_var.set("未知单位")
        return

    # 3. 保留适当小数位并显示
    num_var.set(f"{final:.5g}")  # 5 位有效数字


#MAIN
#Holding frames
#########
root = Tk()
mainframe = Frame(root)

#Widgets
#########
cm_var = StringVar()
cm_entry = Entry(mainframe, font=("Courier", 30), textvariable=cm_var, width=5)

unit_label = Label(mainframe, font=("Courier", 15), text="cm")

num_var = StringVar()
num_label = Label(mainframe, font=("Courier", 30), textvariable=num_var, width=5)

unit_convert_var = StringVar()
unit_convert_spinbox = Spinbox(mainframe, textvariable=unit_convert_var, values=['mm', 'cm', 'm', 'km'])

convert_button = Button(mainframe, text="convert", command=convert_number)

#GRID THE WIDGETS
###########
mainframe.grid(padx = 50, pady = 50)

cm_entry.grid(row=1, column=1)
unit_label.grid(row=2, column=1)
num_label.grid(row=3, column=1)
unit_convert_spinbox.grid(row=4,column=1)
convert_button.grid(row=5, column=1)

root.mainloop()

