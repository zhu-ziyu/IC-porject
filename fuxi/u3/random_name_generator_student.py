from tkinter import *
from tkinter.font import Font
import random



def get_names(filename):
    global all_names
    
    all_names = []

    fileIn = open(filename, encoding='utf-8', errors='replace')

    for line in fileIn:
        all_names.append(line.strip())

    return all_names

def generate_names():
    global all_names, list_var
    # 从 all_names 随机选 10 个不重复的名字
    new_names = random.sample(all_names, 10)
    # 更新绑定的 StringVar，让 Listbox 重载
    list_var.set(new_names)

    


#MAIN
global all_names
get_names("random_names.txt")

root = Tk()
root.config(bg="#293d3d")
mainframe = Frame(root, bg="#293d3d")

sunday_font = Font(family="Sunday", size=20)

title = Label(mainframe, text="Random Names", bg="#293d3d", fg="#ffffff", font=sunday_font)


#create the Listbox widget
list_var = StringVar()
list_var.set(random.choice(all_names))
name_listbox = Listbox(mainframe,listvariable=list_var,selectmode=SINGLE,width=30,height=10,bg="#293d3d",fg="#ffffff")



random_button = Button(mainframe, text="Randomize", highlightbackground="#669999", font=sunday_font, command=generate_names)

#Grid the widgets
mainframe.grid(padx=100, pady=100)
title.grid(row=0, column=1, pady=10)
name_listbox.grid(row=1, column=1, pady=20)
random_button.grid(row=2, column=1, sticky=EW, ipady=10)


root.mainloop()