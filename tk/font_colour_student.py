from tkinter import *
import random

def change_font_colour():
    # 1. 拿到下拉菜单里选中的颜色名
    selected = colour_option_var.get()
    # 2. 更新 Label 上显示的文字
    colour_word_var.set(selected)
    # 3. 直接把名字当 fg 颜色传给 config
    colour_word_label.config(fg=selected)
    # 如果想用 HEX，可以这样：
    # hex_map = {
    #   'black': '#000000', 'grey': '#808080', 'blue': '#0000FF',
    #   'red':   '#FF0000', 'orange': '#FFA500', 'pink': '#FFC0CB',
    #   'green': '#008000'
    # }
    # colour_word_label.config(fg=hex_map[selected])


#MAIN
#Holding frames
#########
root = Tk()
mainframe = Frame(root)

#Widgets
#########
colour_word_var = StringVar()
colour_word_var.set("black")
colour_word_label = Label(mainframe, font=("Arial", 50), fg="#000000", textvariable=colour_word_var)

colours= ['black', 'grey', 'blue', 'red', 'orange', 'pink', 'green']
colour_option_var = StringVar()
colour_option_var.set('black')
colour_option = OptionMenu(mainframe, colour_option_var, *colours)

colour_button = Button(mainframe, text="change", command=change_font_colour)


#GRID THE WIDGETS
###########
mainframe.grid(padx = 50, pady = 50)


colour_option.grid(row=1, column=1, padx=40, ipadx=12)
colour_button.grid(row=2, column=1, padx=40, ipadx=20)
colour_word_label.grid(row=1, column=2, rowspan=2)


root.mainloop()

