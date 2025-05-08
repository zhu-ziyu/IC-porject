from tkinter import *
from tkinter.font import Font

def accept_terms():

    if accept_var.get() == "accept":
        signature_entry.config(state=NORMAL, bg="white")
        accept_button.config(state=NORMAL)
    else:
        signature_entry.config(state=DISABLED, bg="white")
        accept_button.config(state=DISABLED)
        signature_var.set("")

def accept_message():

    name = signature_var.get().strip()
    if name:

        accept_check.deselect()
        signature_entry.config(state=DISABLED, bg="white")
        accept_button.config(state=DISABLED)
        signature_var.set("")
    else:
        # 提醒并将背景设为黄色
        signature_var.set("Please enter your name")
        signature_entry.config(bg="yellow")

def cancel_message():

    accept_check.deselect()
    signature_entry.config(state=DISABLED, bg="white")
    accept_button.config(state=DISABLED)
    signature_var.set("")


root = Tk()
root.title("Terms & Conditions")

mainframe = Frame(root)
mainframe.grid(padx=80, pady=80, sticky=N+S+E+W)


timesFontSmall = Font(family="Times New Roman", size=20)
timesFontLarge = Font(family="Times New Roman", size=30)

titleLabel = Label(mainframe, text="Terms of Agreement", font=timesFontLarge)
titleLabel.grid(row=0, column=1, columnspan=2, sticky=W)

conditions = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tristique quam ut lectus interdum, vitae elementum velit mattis. Proin elit odio, porta at ex id, scelerisque rutrum dui. Vestibulum blandit lectus massa, nec rutrum felis ullamcorper eget. Maecenas molestie odio tellus. Aliquam rutrum euismod metus vitae fringilla. Suspendisse lobortis tellus ac felis porta, sit amet interdum nisi commodo. Donec eros arcu, accumsan sit amet varius a, sollicitudin at massa. Pellentesque vitae imperdiet tortor, vel scelerisque odio. Donec vel ante facilisis, tristique felis non, malesuada urna. Sed faucibus tempus dolor quis condimentum. Suspendisse blandit mattis nulla sit amet imperdiet. Pellentesque dapibus efficitur ullamcorper. Aenean maximus ipsum nec tellus viverra, quis tempor ligula maximus.

Ut ac elit sit amet tortor efficitur aliquam. Morbi felis dui, vestibulum sit amet nulla sit amet, elementum consequat lorem. Nulla semper massa nec massa eleifend, non luctus mi auctor. Aliquam suscipit arcu vel viverra convallis. Mauris turpis odio, finibus sed mi sed, lobortis eleifend dui. Morbi dignissim facilisis augue at hendrerit. Nullam tempus volutpat est, ut aliquam neque iaculis quis. Quisque et nisl sed orci fringilla condimentum finibus id nulla.

Ut rutrum malesuada eleifend. Praesent nunc lorem, vulputate vulputate purus vel, aliquam aliquet metus. Duis pharetra venenatis turpis dictum laoreet. Phasellus ut nulla a libero fermentum mollis. Proin maximus bibendum turpis ut cursus. Duis id consequat magna, eget elementum nunc. Integer molestie nulla justo, nec venenatis ipsum eleifend a.

Maecenas enim justo, lobortis ut efficitur et, mollis vitae nisi. In ac erat elementum, pulvinar quam vitae, sagittis leo. In placerat commodo arcu a lobortis. Sed aliquam aliquam urna a blandit. Sed venenatis, lorem sit amet pharetra ornare, arcu nisl venenatis ex, eget euismod elit justo sit amet purus. In ullamcorper mauris non mattis molestie. In dapibus ultrices dolor, ut bibendum magna bibendum non. Nunc risus sapien, iaculis nec neque in, venenatis aliquet leo. Nam porta maximus lectus, sit amet interdum purus convallis quis. Proin ultricies, ipsum eu auctor varius, leo erat vehicula elit, at suscipit ex erat sit amet nisi. Fusce at tristique dolor. Morbi fringilla, lacus a lobortis placerat, felis nisl porta elit, ut laoreet odio enim gravida quam. Quisque rhoncus porttitor fringilla. Donec sit amet tempor ex.

Fusce auctor augue id orci facilisis, sed molestie metus laoreet. Donec consectetur finibus libero id imperdiet. Nullam efficitur mauris sit amet gravida vulputate. Sed tristique mi in purus fermentum, sed volutpat lorem pellentesque. Duis id lacus in ligula aliquet porta. Aliquam quis pellentesque elit, quis commodo urna. Donec malesuada ut lorem sed tempor. Mauris at ipsum nunc.
"""
conditionsText = Text(mainframe, bg="#eeeeee", height=8, bd=10, wrap=WORD)
conditionsText.insert(END, conditions)
conditionsText.config(state=DISABLED)  # 不允许编辑
conditionsText.grid(row=1, column=1, columnspan=2, pady=(10,50))


accept_var = StringVar()
accept_check = Checkbutton(
    mainframe,
    text="I accept the Terms & Conditions",
    variable=accept_var,
    onvalue="accept", offvalue="",
    font=timesFontSmall,
    command=accept_terms
)
accept_check.grid(row=2, column=1, columnspan=2, sticky=E)


signature_var = StringVar()
signature_entry = Entry(
    mainframe,
    textvariable=signature_var,
    state=DISABLED,
    font=timesFontSmall
)
signature_entry.grid(row=3, column=1, columnspan=2, sticky=EW, pady=(10,30))

cancel_button = Button(mainframe, text="Cancel", command=cancel_message)
cancel_button.grid(row=4, column=1, ipadx=10, ipady=5, padx=10, sticky=EW)

accept_button = Button(mainframe, text="Accept", state=DISABLED, command=accept_message)
accept_button.grid(row=4, column=2, ipadx=10, ipady=5, padx=10, sticky=EW)


root.mainloop()
