from tkinter import *
import random

def change_colour(ignore):

    r = red.get()
    g = green.get()
    b = blue.get()
    hexcol = f'#{r:02x}{g:02x}{b:02x}'
    colour_var.set(hexcol)           # 更新 Label 上的文本
    colour_frame.config(bg=hexcol)   # 更新右侧方块的背景

        
#MAIN
#Holding frames
#########
root = Tk()
mainframe = Frame(root)
colour_frame = Frame(root)

#Widgets
#########
red = IntVar(value=0)
green = IntVar(value=0)
blue = IntVar(value=0)

red_scale = Scale(
    mainframe,
    from_=0, to=255,
    orient=HORIZONTAL,
    variable=red,
    command=change_colour
)
green_scale = Scale(
    mainframe,
    from_=0, to=255,
    orient=HORIZONTAL,
    variable=green,
    command=change_colour
)
blue_scale = Scale(
    mainframe,
    from_=0, to=255,
    orient=HORIZONTAL,
    variable=blue,
    command=change_colour
)


colour_var = StringVar()
colour_var.set("#000000")
colour_label = Label(mainframe, textvariable = colour_var)

#GRID THE WIDGETS
###########

mainframe.grid(row=1, column=1, padx=20)
colour_frame.grid(row = 1, column=2, pady=20, padx=20, ipadx=100, ipady=100)

red_scale.grid(row=1, column=1, sticky="ew")
green_scale.grid(row=2, column=1, sticky="ew")
blue_scale.grid(row=3, column=1, sticky="ew")
# 现有的 colour_label 放在第 4 行
colour_label.grid(row=4, column=1)



colour_label.grid(row=4, column=1)


root.mainloop()

