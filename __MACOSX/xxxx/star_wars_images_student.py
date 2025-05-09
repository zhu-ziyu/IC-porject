from tkinter import *
from tkinter.font import Font
from operator import itemgetter



def load_images():
    global image_list
    rey_photo = PhotoImage(file="rey.png")
    bb8_photo = PhotoImage(file="bb8.png")
    c3po_photo = PhotoImage(file="c3po.png")
    finn_photo = PhotoImage(file="finn.png")
    poe_photo = PhotoImage(file="poe.png")

    image_list = [rey_photo, bb8_photo, c3po_photo, finn_photo, poe_photo]


def change_image():
    global image_list
    sel = images_listbox.curselection()
    if sel:
        idx = sel[0]
        img = image_list[idx]
        current_image_label.config(image=img)
        current_image_label.image = img


#MAIN
#Holding frames
#########

root = Tk()
mainframe = Frame(root)

starwars_fontsmall = Font(family="Star Jedi", size=15)
starwars_font = Font(family="Star Jedi", size=30)

global image_list
load_images()
image_names = ['Rey', 'BB-8', 'C-3Po', 'Finn', 'Poe']



#Widgets
#########
title = Label(mainframe, text="star wars", font=starwars_font)

images_var = StringVar(value=image_names)
images_listbox = Listbox(mainframe, listvariable=images_var, selectmode=SINGLE, font=starwars_fontsmall)

# set default selection to BB-8 (index 1)
images_listbox.selection_set(1)

current_image_label = Label(mainframe)
# display BB-8 image by default
current_image_label.config(image=image_list[1])
current_image_label.image = image_list[1]

update_button = Button(mainframe, text="SEE", command=change_image)

#GRID THE WIDGETS
###########

mainframe.grid(padx=50, pady=50)
title.grid(row=1, column=1, sticky=W, padx = 20, pady=5)
images_listbox.grid(row=2, column=1, padx=10)
current_image_label.grid(row=2, column=2, sticky=W, padx=10, pady=10)
update_button.grid(row=3, column=1, ipady=20, ipadx=40, padx=10, pady=10, sticky=E)

root.mainloop()
