from tkinter import *
from tkinter.font import Font
import random

def random_roll():
    global previous_score, num_turns

    current_score = score_var.get()
    roll = random.randint(1, 6)
    num_turns += 1


    value_var.set(str(roll))

    if roll == 1:
        # bust — back to last held total
        score_var.set(previous_score)
        score_scale.config(troughcolor='red')
    else:
        # add roll to current turn total
        score_var.set(current_score + roll)
        score_scale.config(troughcolor='blue')

    check_win()


def check_win():

    if score_var.get() >= 100:
        result_var.set(f"🎉 You win in {num_turns} turns!")
        roll_button.config(state='disabled')
        hold_button.config(state='disabled')


def hold():
    global previous_score
    # lock in your current total
    previous_score = score_var.get()
    # give a visual cue
    score_scale.config(troughcolor='#1b8233')


# MAIN
previous_score = 0
num_turns = 0

root = Tk()
mainframe = Frame(root)

big_font   = Font(family='Arial',        size=80)
med_font   = Font(family='Guinea Pigs',  size=40)
small_font = Font(family='Guinea Pigs',  size=20)
num_font   = Font(family='Arial',        size=20)


title_label = Label(mainframe, text='GAME OF PIG', font=med_font)

roll_button = Button(mainframe, text='ROLL', font=small_font, command=random_roll)
hold_button = Button(mainframe, text='HOLD', font=small_font, command=hold)

value_var   = StringVar(value='0')
value_label = Label(mainframe, textvariable=value_var, font=big_font)

score_var   = IntVar(value=0)
score_scale = Scale(mainframe,
                    from_=0, to=100,
                    variable=score_var,
                    width=50, length=350,
                    orient=HORIZONTAL)

result_var   = StringVar()
result_label = Label(mainframe, textvariable=result_var, font=num_font)

# Layout

mainframe.grid(padx=100, pady=100)

title_label.grid(row=1, column=1, columnspan=2, sticky=W)
score_scale.grid(row=2, column=1, columnspan=2, pady=20)

roll_button.grid(row=3, column=1, ipady=20, sticky=EW)
hold_button.grid(row=4, column=1, ipady=20, sticky=EW)
value_label.grid(row=3, column=2, rowspan=2, padx=20)

result_label.grid(row=5, column=1, columnspan=2, pady=40)

root.mainloop()
