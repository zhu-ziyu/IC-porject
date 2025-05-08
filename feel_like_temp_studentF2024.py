from tkinter import *
from tkinter.font import Font

def change_temp(event=None):
    t = temp_var.get()
    v = speed_var.get()
    # compute wind chill
    w = 13.12 + 0.6215 * t - 11.37 * (v ** 0.16) + 0.3965 * t * (v ** 0.16)
    # update the label, rounded to one decimal, with a degree symbol
    feel_like_var.set(f"Feels like: {w:.1f} \u00B0C")

root = Tk()
root.title("Wind Chill Calculator")


mainframe = Frame(root, padx=30, pady=40)
mainframe.grid()


arial_font_large = Font(family="Arial", size=30)
arial_font_small = Font(family="Arial", size=18)


title_label = Label(mainframe, text="Wind Chill Calculator", font=arial_font_small)

temp_var = IntVar(value=0)
temp_scale = Scale(mainframe, from_=30, to=-20, variable=temp_var,
                   orient=VERTICAL, command=change_temp)
temp_label = Label(mainframe, text="temp")

speed_var = IntVar(value=0)
speed_scale = Scale(mainframe, from_=40, to=0, variable=speed_var,
                    orient=VERTICAL, command=change_temp)
wind_label = Label(mainframe, text="wind")

feel_like_var = StringVar()
feel_like_label = Label(mainframe, textvariable=feel_like_var,
                        font=arial_font_large)

title_label.grid(row=0, column=0, columnspan=3, pady=(0,20))

temp_scale.grid(row=1, column=0, padx=5)
speed_scale.grid(row=1, column=1, padx=5)
feel_like_label.grid(row=1, column=2, padx=(30,0))

temp_label.grid(row=2, column=0)
wind_label.grid(row=2, column=1)

# initialize the feels-like display
change_temp()

root.mainloop()
