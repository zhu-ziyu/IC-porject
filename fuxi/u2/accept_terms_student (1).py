from tkinter import *
from tkinter.font import Font
from tkinter.messagebox import *


def accept_terms():
    # 检查 Checkbutton 是否被选中
    if accept_var.get() == "accept":
        # 如果选中了，就启用签名 Entry 和 Accept 按钮
        signature_entry.config(state=NORMAL, bg="white")
        accept_button .config(state=NORMAL)
    else:
        # 如果取消选中，就禁用签名框和 Accept 按钮
        signature_entry.config(state=DISABLED, bg="white")
        accept_button.config(state=DISABLED)

        
def accept_message():
    name = signature_var.get().strip()   # 读取用户输入并去掉前后空格
    if name:
        # 用户已经签名 —— 弹窗提示，或者直接打印，题目没强制
        showinfo("Thank you", f"Thanks, {name}!")
        # 然后重置所有控件回初始状态
        accept_check.deselect()            # 取消勾选
        accept_terms()                     # 复用上面函数，把 Entry 和按钮禁用
    else:
        # 用户还没输入名字
        signature_entry.config(bg="#ffdddd")  # 浅红背景提醒
        signature_entry.focus()

def cancel_message():
    # 直接把所有东西都重置到默认
    accept_check.deselect()                # 取消复选
    signature_entry.delete(0, END)         # 清空签名框
    signature_entry.config(state=DISABLED, bg="white")
    accept_button.config(state=DISABLED)   # 禁用 Accept 按钮




#MAIN
root = Tk()
mainframe = Frame(root)

timesFontSmall = Font(family="Times New Roman", size=20)
timesFontLarge = Font(family="Times New Roman", size=30)

#Create the widgets
titleLabel = Label(mainframe, text="Terms of Agreement", font=timesFontLarge)
conditions = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tristique quam ut lectus interdum, vitae elementum velit mattis. Proin elit odio, porta at ex id, scelerisque rutrum dui. Vestibulum blandit lectus massa, nec rutrum felis ullamcorper eget. Maecenas molestie odio tellus. Aliquam rutrum euismod metus vitae fringilla. Suspendisse lobortis tellus ac felis porta, sit amet interdum nisi commodo. Donec eros arcu, accumsan sit amet varius a, sollicitudin at massa. Pellentesque vitae imperdiet tortor, vel scelerisque odio. Donec vel ante facilisis, tristique felis non, malesuada urna. Sed faucibus tempus dolor quis condimentum. Suspendisse blandit mattis nulla sit amet imperdiet. Pellentesque dapibus efficitur ullamcorper. Aenean maximus ipsum nec tellus viverra, quis tempor ligula maximus.\n\nUt ac elit sit amet tortor efficitur aliquam. Morbi felis dui, vestibulum sit amet nulla sit amet, elementum consequat lorem. Nulla semper massa nec massa eleifend, non luctus mi auctor. Aliquam suscipit arcu vel viverra convallis. Mauris turpis odio, finibus sed mi sed, lobortis eleifend dui. Morbi dignissim facilisis augue at hendrerit. Nullam tempus volutpat est, ut aliquam neque iaculis quis. Quisque et nisl sed orci fringilla condimentum finibus id nulla.\n\nUt rutrum malesuada eleifend. Praesent nunc lorem, vulputate vulputate purus vel, aliquam aliquet metus. Duis pharetra venenatis turpis dictum laoreet. Phasellus ut nulla a libero fermentum mollis. Proin maximus bibendum turpis ut cursus. Duis id consequat magna, eget elementum nunc. Integer molestie nulla justo, nec venenatis ipsum eleifend a.\n\nMaecenas enim justo, lobortis ut efficitur et, mollis vitae nisi. In ac erat elementum, pulvinar quam vitae, sagittis leo. In placerat commodo arcu a lobortis. Sed aliquam aliquam urna a blandit. Sed venenatis, lorem sit amet pharetra ornare, arcu nisl venenatis ex, eget euismod elit justo sit amet purus. In ullamcorper mauris non mattis molestie. In dapibus ultrices dolor, ut bibendum magna bibendum non. Nunc risus sapien, iaculis nec neque in, venenatis aliquet leo. Nam porta maximus lectus, sit amet interdum purus convallis quis. Proin ultricies, ipsum eu auctor varius, leo erat vehicula elit, at suscipit ex erat sit amet nisi. Fusce at tristique dolor. Morbi fringilla, lacus a lobortis placerat, felis nisl porta elit, ut laoreet odio enim gravida quam. Quisque rhoncus porttitor fringilla. Donec sit amet tempor ex.\n\nFusce auctor augue id orci facilisis, sed molestie metus laoreet. Donec consectetur finibus libero id imperdiet. Nullam efficitur mauris sit amet gravida vulputate. Sed tristique mi in purus fermentum, sed volutpat lorem pellentesque. Duis id lacus in ligula aliquet porta. Aliquam quis pellentesque elit, quis commodo urna. Donec malesuada ut lorem sed tempor. Mauris at ipsum nunc."
conditionsText = Text(mainframe, bg="#eeeeee", height=8, bd=10)
conditionsText.insert(END, conditions)

accept_var = StringVar()
accept_check = Checkbutton(mainframe, \
                          text="I accept the Terms & Conditions", \
                          variable=accept_var, \
                          onvalue="accept", offvalue="false", \
                          font=timesFontSmall, command=accept_terms)

signature_var = StringVar()
signature_entry = Entry(mainframe, textvariable=signature_var, state=DISABLED, font=timesFontSmall)

accept_button = Button(mainframe, text="Accept", state=DISABLED, command=accept_message)
cancel_button = Button(mainframe, text="Cancel", command=cancel_message)


#GRID the widgets
mainframe.grid(padx=80, pady=80)
titleLabel.grid(row=0, column=1, columnspan=2, sticky=W)
conditionsText.grid(row=1, column=1, columnspan=2)
accept_check.grid(row=2, column=1, columnspan=2, sticky=E, pady=(50, 5))
signature_entry.grid(row=3, column=2, columnspan=2, sticky=EW, pady=(0, 50))

cancel_button.grid(row=4, column=1, ipady=10, padx=10, sticky=EW)
accept_button.grid(row=4, column=2, ipady=10, padx=10, sticky=EW)


root.mainloop()

