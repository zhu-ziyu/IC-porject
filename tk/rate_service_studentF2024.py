from tkinter import *
from tkinter.font import Font
import random

def change_service_level(valume):
     level =int(valume)
     if level == 1:
          service_level_var.set("Good")
     elif level == 2:
          service_level_var.set("Bad")
     else:
          service_level_var.set("Normal")



#MAIN
#Holding frames
#########
root = Tk()
mainframe = Frame(root)

arial_font = Font(family="Arial", size=20)

#Widgets
#########


service_scale = Scale(mainframe,from_=0,to=5,orient=HORIZONTAL,command=change_service_level)

service_level_var = StringVar()
service_level_var.set("Normal")
service_level_label = Label(mainframe, textvariable = service_level_var, font=arial_font)

#GRID THE WIDGETS
###########

mainframe.grid(row=1, column=1, padx=100, pady=50)


service_level_label.grid(row=1, column=2, sticky=E)
service_scale.grid(row=2, column=1, columnspan=2, ipadx=50)



root.mainloop()



