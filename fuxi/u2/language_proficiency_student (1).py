from tkinter import *

def calculate_proficiency():
    count = 0
    for var in all_checkvars:
        if var.get() == 1:
            count += 1
    if count == 1:
        level = "Expert"
    if count == 2:
        level = "Competent"
    if count == 3:
        level = "Novice"
    if count == 4:
        level = "Expert"
    if count == 5:
        level = "Competent"
    proficiency_var.set(level)


#MAIN
global all_checkvars

root = Tk()
mainframe = Frame(root)
language_frame = LabelFrame(mainframe, text="check your languages")

#Create the widgets
title_label = Label(mainframe, text="Language Proficiency", font=("Arial, 20"))


# 左列语言
javascript_var = IntVar(value=0)
javascript_check = Checkbutton(language_frame, text="JavaScript",
                               variable=javascript_var, onvalue=1, offvalue=0)
javascript_check.grid(row=1, column=0, sticky=W)

python_var = IntVar(value=0)
python_check = Checkbutton(language_frame, text="Python",
                           variable=python_var, onvalue=1, offvalue=0)
python_check.grid(row=2, column=0, sticky=W)

java_var = IntVar(value=0)
java_check = Checkbutton(language_frame, text="Java",
                         variable=java_var, onvalue=1, offvalue=0)
java_check.grid(row=3, column=0, sticky=W)

php_var = IntVar(value=0)
php_check = Checkbutton(language_frame, text="PHP",
                        variable=php_var, onvalue=1, offvalue=0)
php_check.grid(row=4, column=0, sticky=W)

# 右列语言
cpp_var = IntVar(value=0)
cpp_check = Checkbutton(language_frame, text="C++",
                        variable=cpp_var, onvalue=1, offvalue=0)
cpp_check.grid(row=1, column=1, sticky=W, padx=20)

csharp_var = IntVar(value=0)
csharp_check = Checkbutton(language_frame, text="C#",
                           variable=csharp_var, onvalue=1, offvalue=0)
csharp_check.grid(row=2, column=1, sticky=W, padx=20)

ruby_var = IntVar(value=0)
ruby_check = Checkbutton(language_frame, text="Ruby",
                         variable=ruby_var, onvalue=1, offvalue=0)
ruby_check.grid(row=3, column=1, sticky=W, padx=20)

css_var = IntVar(value=0)
css_check = Checkbutton(language_frame, text="CSS",
                        variable=css_var, onvalue=1, offvalue=0)
css_check.grid(row=4, column=1, sticky=W, padx=20)

all_checkvars = [
    javascript_var, python_var, java_var, php_var,
    cpp_var, csharp_var, ruby_var, css_var
]
calculate_button = Button(mainframe, text="Calculate", command=calculate_proficiency)

proficiency_var = StringVar()
proficiency_label = Label(mainframe, textvariable=proficiency_var, font=("Arial, 20"))

javascript_var=IntVar()
javascript=Checkbutton(mainframe,)

#GRID the widgets
mainframe.grid(padx=50, pady=50)
title_label.grid(row=1, column=1, pady=10, sticky=W)

language_frame.grid(row=2, column=1, ipadx=20, ipady=20)

calculate_button.grid(row=3, column=1, ipady=2, pady=20, sticky=EW)

proficiency_label.grid(row=4, column=1, pady=20, sticky=W)

root.mainloop()

