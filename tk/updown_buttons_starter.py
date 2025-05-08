from tkinter import *
from tkinter.font import Font

def increase_value():
    global value
    value += 1
    value_var.set(f'{value:^6}')

def decrease_value():
    global value
    value -= 1
    value_var.set(f'{value:^6}')

# MAIN
value = 10

root = Tk()
mainframe = Frame(root)
mainframe.grid(padx=100, pady=100)

# Fonts
big_font   = Font(family="Fresh Fruit", size=100)
small_font = Font(family="Fresh Fruit", size=30)

# Widgets
title_label    = Label(mainframe, text="COUNTER", font=small_font)
decrease_button= Button(mainframe, text="-", font=big_font, command=decrease_value)
increase_button= Button(mainframe, text="+", font=big_font, command=increase_value)

value_var   = StringVar(value=f'{value:^6}')
value_label = Label(mainframe, textvariable=value_var, font=big_font)

# Layout with grid
title_label   .grid(row=0, column=0, columnspan=2, pady=(0,20))
value_label   .grid(row=1, column=0, columnspan=2, pady=(0,20))
decrease_button.grid(row=2, column=0, padx=(0,10))
increase_button.grid(row=2, column=1, padx=(10,0))

root.mainloop()
