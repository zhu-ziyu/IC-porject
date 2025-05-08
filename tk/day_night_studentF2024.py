from tkinter import *
from tkinter.font import Font
import random

def change_day_night(ignore):
    time=day_night_var.get()
    if time == 1:
        word_var.set("on")
        bg = "#F0E68C"
    else:
        word_var.set("off")
   

#MAIN
#HOlding frames
#########
root = Tk()
mainframe = Frame(root)

arial_font = Font(family="Arial", size=40)

#Widgets
#########

day_night_var = IntVar()
day_night_var.set(1)
day_night_scale = Scale(mainframe, variable=day_night_var, \
                      width=50, length=100, \
                      from_=1, to=2, \
                      showvalue=False, \
                      orient=HORIZONTAL, \
                      command=change_day_night)                         

word_var = StringVar()
word_var.set("ON")
word_label = Label(mainframe, textvariable=word_var, font=arial_font)


#GRID THE WIDGETS
###########
mainframe.grid(row=1, column=1, padx=100, pady=100)

word_label.grid(row=1, column=1)
day_night_scale.grid(row=2, column=1)



root.mainloop()

