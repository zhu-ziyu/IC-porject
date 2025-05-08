from tkinter import *
from tkinter.font import Font

def change_service_level(ignore):
    levels = {
        1: "Could be better",
        2: "Below Average",
        3: "Normal",
        4: "Good",
        5: "Excellent"
    }
    service_level_var.set(levels[service_scale.get()])

# MAIN
root = Tk()
mainframe = Frame(root)
mainframe.grid(row=1, column=1, padx=100, pady=50)

arial_font = Font(family="Arial", size=20)

# scale + label
service_scale = Scale(
    mainframe,
    from_=1, to=5,
    orient=HORIZONTAL,
    showvalue=False,
    command=change_service_level
)
service_level_var = StringVar(value="Normal")
service_level_label = Label(mainframe, textvariable=service_level_var, font=arial_font)

# layout
service_level_label.grid(row=1, column=2, sticky=E)
service_scale.grid(row=2, column=1, columnspan=2, ipadx=50)

root.mainloop()
