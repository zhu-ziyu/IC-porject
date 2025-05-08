from tkinter import *
import random

import datetime

def calculate_age():

    #day =  #get the day from the GUI
    #month = pass #get the month from the GUI
    #year = pass #get the year from the GUI
    
    today = datetime.datetime.today()
    #You can access today.month and today.day to make the calculation more accurate
    #Consider that birthdays after today should show the correct age
    print(f'Testing month: {today.month}, day: {today.day}')
    

    #Calculate the correct age
    age = today.year - year
    


    #update the GUI to display the age



#MAIN
#Holding frames
#########
root = Tk()
mainframe = Frame(root)

#Widgets
#########


month_label = Label(mainframe, text="month")
month_var = IntVar()
month_var.set(10)
month_spinbox = Spinbox(mainframe, width=10, textvariable=month_var, from_=1, to=12)




age_button = Button(mainframe, text="age", command=calculate_age)


            


#GRID THE WIDGETS
###########
mainframe.grid(padx = 100, pady = 100)

month_label.grid(row=1, column=1)
month_spinbox.grid(row=1, column=2, pady=10)

age_button.grid(row=1, column=3, rowspan = 3, padx=20, ipadx=40, sticky=N+S)



root.mainloop()

