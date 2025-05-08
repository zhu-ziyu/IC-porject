from tkinter import *
from tkinter.font import Font
import random

def change_temp(ignore):

    pass
 
        



#MAIN
#########
root = Tk()
mainframe = Frame(root)

arial_font_large = Font(family="Arial", size=30)
arial_font_small = Font(family="Arial", size=18)

#Widgets
#########

title_label = Label(mainframe, text="Wind Chill Calculator", font=arial_font_small)

temp_label = Label(mainframe, text="temp")

temp_var = IntVar()
temp_scale = Scale(mainframe, from_=30, to=-20, variable = temp_var, orient=VERTICAL)
temp_scale.bind("<ButtonRelease-1>", change_temp)

wind_label = Label(mainframe, text="wind")

speed_var = IntVar()
speed_scale = Scale(mainframe, from_=40, to =0, variable = speed_var, orient=VERTICAL)
speed_scale.bind("<ButtonRelease-1>", change_temp)

feel_like_var = StringVar()
feel_like_var.set("Feels like:")
feel_like_label = Label(mainframe, textvariable=feel_like_var, font=arial_font_large, )


#GRID THE WIDGETS
###########

mainframe.grid(row=1, column=1, padx=30, pady=40)




root.mainloop()

