from tkinter import *
from tkinter.font import Font

def clear_receipt():
    global total, receipt
    total = 0
    receipt = ''
    total_var.set(f'${total:.2f}')
    receipt_var.set(receipt)

def add_item(amount, text):
    global total, receipt
    total += amount
    receipt += f'\n{text} - ${amount:.2f}'
    total_var.set(f'${total:.2f}')
    receipt_var.set(receipt)

def coffee():    add_item(2.50, "Coffee")
def tea():       add_item(3.00, "Tea")
def drink():     add_item(1.75, "Soft Drink")
def sandwich():  add_item(5.00, "Sandwich")
def sweet():     add_item(2.25, "Sweet Treat")
def bakery():    add_item(3.25, "Bakery Item")


# ——— 主程序 ———
total = 0
receipt = ''

root = Tk()
root.title("Cafe")
mainframe = Frame(root)
mainframe.grid(padx=50, pady=50)

cafe_small = Font(family="House Home", size=40)
cafe_large = Font(family="House Home", size=80)

# 1) 先加载图片
coffee_photo   = PhotoImage(file="coffee.png")
tea_photo      = PhotoImage(file="tea.png")
drink_photo    = PhotoImage(file="drink.png")
sandwich_photo = PhotoImage(file="sandwich.png")
sweet_photo    = PhotoImage(file="sweet.png")
bakery_photo   = PhotoImage(file="bakery.png")

# 2) 再创建按钮，并绑定图片
coffee_button  = Button(mainframe, image=coffee_photo, command=coffee)
tea_button     = Button(mainframe, image=tea_photo,    command=tea)
drink_button   = Button(mainframe, image=drink_photo,  command=drink)
sandwich_button= Button(mainframe, image=sandwich_photo, command=sandwich)
sweet_button   = Button(mainframe, image=sweet_photo,  command=sweet)
bakery_button  = Button(mainframe, image=bakery_photo, command=bakery)

# 3) 其他控件
clear_button = Button(mainframe, text='Clear', font=cafe_small, command=clear_receipt)
title_label  = Label(mainframe, text="CAFE", font=cafe_small)

total_var     = StringVar(value=f'${total:.2f}')
total_label   = Label(mainframe, textvariable=total_var, font=cafe_large)

receipt_var   = StringVar()
receipt_label = Label(mainframe, textvariable=receipt_var, font=cafe_small, justify=LEFT)

# 4) 最后 grid 布局
title_label    .grid(row=1, column=1, sticky=W)
total_label    .grid(row=1, column=2, columnspan=2, sticky=E)

coffee_button  .grid(row=2, column=1, padx=5, pady=5)
tea_button     .grid(row=2, column=2, padx=5, pady=5)
drink_button   .grid(row=2, column=3, padx=5, pady=5)
sandwich_button.grid(row=3, column=1, padx=5, pady=5)
sweet_button   .grid(row=3, column=2, padx=5, pady=5)
bakery_button  .grid(row=3, column=3, padx=5, pady=5)

clear_button   .grid(row=4, column=1, columnspan=3, sticky=EW, pady=(10,0))
receipt_label  .grid(row=5, column=1, columnspan=3, sticky=W)

root.mainloop()
