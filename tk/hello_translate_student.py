from tkinter import *
import random


def translate_hello():

    texte = hello_var.get()
    # 一定要这样“调用” set()，而不是赋值
    word_var.set(texte)

#MAIN
#Holding frames
#########
root = Tk()
mainframe = Frame(root)

#Widgets
#########
word_var = StringVar()
word_var.set("hello")
hello_label = Label(mainframe, font=("Courier", 50), textvariable=word_var)

hello_list=["hello","nihao"]
hello_var = StringVar()
hello_var.set("hello")
hello_liebiao =OptionMenu(mainframe,hello_var, *hello_list)



change_button = Button(mainframe, text='translate', command = translate_hello)

#GRID THE WIDGETS
###########
mainframe.grid(padx = 50, pady = 50)

hello_liebiao.grid(row=2, column=1)

hello_label.grid(row=1, column=1)
change_button.grid(row=3, column=1, padx=40, ipadx=25)


root.mainloop()

