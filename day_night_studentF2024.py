from tkinter import *
from tkinter.font import Font

def change_day_night(event=None):
    if day_night_var.get() == 1:
        bg = "#F0E68C"
        fg = "black"
        word_var.set("ON")
    else:
        bg = "#001F54"
        fg = "white"
        word_var.set("OFF")

    root.config(bg=bg)
    mainframe.config(bg=bg)

    word_label.config(bg=bg, fg=fg)

    day_night_scale.config(bg=bg, fg=fg, troughcolor=bg, highlightbackground=bg)

# MAIN
root = Tk()
root.title("Day / Night Toggle")

mainframe = Frame(root)
mainframe.grid(padx=100, pady=100)

arial_font = Font(family="Arial", size=40)


day_night_var = IntVar(value=1)
day_night_scale = Scale(
    mainframe,
    variable=day_night_var,
    width=50, length=100,
    from_=1, to=2,
    showvalue=False,
    orient=HORIZONTAL,
    command=change_day_night
)

word_var = StringVar(value="ON")
word_label = Label(mainframe, textvariable=word_var, font=arial_font)

# layout
word_label.grid(row=0, column=0, pady=(0,20))
day_night_scale.grid(row=1, column=0)

# initialize colors
change_day_night()

root.mainloop()
