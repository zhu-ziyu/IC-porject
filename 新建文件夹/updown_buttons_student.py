from tkinter import *
from tkinter.font import Font

def increase_value():
    global value

    value += stepVar.get()
    value_var.set(f'{value:^6}')

def decrease_value():
    global value

    value -= stepVar.get()
    value_var.set(f'{value:^6}')


value = 10  # starting total

big_font   = ("Helvetica", 50)
small_font = ("Helvetica", 20)

root = Tk()
root.title("Add/Subtract Demo")

mainframe = Frame(root)
mainframe.grid(padx=100, pady=100)


decrease_button = Button(mainframe, text="-", font=big_font, command=decrease_value)
decrease_button.grid(row=1, column=1, ipadx=25, ipady=10)

value_var   = StringVar(value=f'{value:^6}')
value_label = Label(mainframe, textvariable=value_var, font=big_font)
value_label.grid(row=1, column=2, padx=20)

increase_button = Button(mainframe, text="+", font=big_font, command=increase_value)
increase_button.grid(row=1, column=3, ipadx=20, ipady=10)


other_frame = LabelFrame(mainframe, text="increment/decrement amount")
other_frame.grid(row=2, column=1, columnspan=3, pady=20, sticky=EW)

stepVar = IntVar(value=1)

# build the four radios
Radiobutton(other_frame, text="1",  variable=stepVar, value=1,  font=small_font).grid(row=1, column=1, padx=60, sticky=W)
Radiobutton(other_frame, text="2",  variable=stepVar, value=2,  font=small_font).grid(row=2, column=1, padx=60, sticky=W)
Radiobutton(other_frame, text="5",  variable=stepVar, value=5,  font=small_font).grid(row=1, column=2, sticky=W)
Radiobutton(other_frame, text="10", variable=stepVar, value=10, font=small_font).grid(row=2, column=2, sticky=W)

root.mainloop()
