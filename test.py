from tkinter import *

root = Tk()
root.title("Contact Manager")

mainframe = Frame(root)
mainframe.grid(padx=30, pady=30)

# 创建控件
nameLabel    = Label(mainframe, text="Name")
nameEntry    = Entry(mainframe, width=30)
phoneLabel   = Label(mainframe, text="顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶ddddddddddddddddddddd")
phoneEntry   = Entry(mainframe, width=30)

addButton    = Button(mainframe, text="Add")
updateButton = Button(mainframe, text="Update")
deleteButton = Button(mainframe, text="Delete")

# 摆放控件
# 第一行：Name 标签 + 输入框（横跨2列）
nameLabel   .grid(row=0, column=0, sticky=E, padx=5, pady=5)
nameEntry   .grid(row=0, column=1, columnspan=2, sticky=W, padx=5, pady=5)

# 第二行：Phone 标签 + 输入框（横跨2列）
phoneLabel  .grid(row=1, column=0, sticky=E, padx=5, pady=5)
phoneEntry  .grid(row=1, column=1, columnspan=2, sticky=W, padx=5, pady=5)

# 第三行：三个按钮，分别放在列 0、1、2
addButton    .grid(row=2, column=0, padx=5, pady=10)
updateButton .grid(row=2, column=1, padx=5, pady=10)
deleteButton .grid(row=2, column=2, padx=5, pady=10)

root.mainloop()
