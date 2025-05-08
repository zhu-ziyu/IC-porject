from tkinter import *

def calculate_proficiency():


    count = sum(var.get() for var in all_checkvars)

    if count >= 6:
        level = "Expert"
    elif count >= 3:
        level = "Competent"
    else:
        level = "Novice"
    proficiency_var.set(level)


root = Tk()
root.title("Language Proficiency")

mainframe = Frame(root)
mainframe.grid(padx=50, pady=50)


title_label = Label(mainframe, text="Language Proficiency", font=("Arial", 20))
title_label.grid(row=1, column=1, pady=10, sticky=W)


language_frame = LabelFrame(mainframe, text="check your languages")
language_frame.grid(row=2, column=1, ipadx=20, ipady=20)


javascript_var = IntVar()
python_var     = IntVar()
java_var       = IntVar()
php_var        = IntVar()

javascript_check = Checkbutton(language_frame, text="JavaScript", variable=javascript_var)
python_check     = Checkbutton(language_frame, text="Python",     variable=python_var)
java_check       = Checkbutton(language_frame, text="Java",       variable=java_var)
php_check        = Checkbutton(language_frame, text="PHP",        variable=php_var)

javascript_check.grid(row=1, column=1, sticky=W, padx=10, pady=2)
python_check    .grid(row=2, column=1, sticky=W, padx=10, pady=2)
java_check      .grid(row=3, column=1, sticky=W, padx=10, pady=2)
php_check       .grid(row=4, column=1, sticky=W, padx=10, pady=2)

cplusplus_var = IntVar()
csharp_var    = IntVar()
ruby_var      = IntVar()
css_var       = IntVar()

cplusplus_check = Checkbutton(language_frame, text="C++", variable=cplusplus_var)
csharp_check    = Checkbutton(language_frame, text="C#",  variable=csharp_var)
ruby_check      = Checkbutton(language_frame, text="Ruby", variable=ruby_var)
css_check       = Checkbutton(language_frame, text="CSS",  variable=css_var)

cplusplus_check.grid(row=1, column=2, sticky=W, padx=10, pady=2)
csharp_check   .grid(row=2, column=2, sticky=W, padx=10, pady=2)
ruby_check     .grid(row=3, column=2, sticky=W, padx=10, pady=2)
css_check      .grid(row=4, column=2, sticky=W, padx=10, pady=2)


all_checkvars = [
    javascript_var, python_var, java_var, php_var,
    cplusplus_var, csharp_var, ruby_var, css_var
]


calculate_button = Button(mainframe, text="Calculate", command=calculate_proficiency)
calculate_button.grid(row=3, column=1, ipady=5, pady=20, sticky=EW)

proficiency_var   = StringVar()
proficiency_label = Label(mainframe, textvariable=proficiency_var, font=("Arial", 20))
proficiency_label.grid(row=4, column=1, pady=10, sticky=W)

root.mainloop()
