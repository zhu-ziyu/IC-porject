from tkinter import *
import random

def getNewQuestion():
    numberOneStringVar.set(random.randint(1, 10))
    numberTwoStringVar.set(random.randint(1, 10))
 


def checkAnswer():
    n1=int(numberOneStringVar.get())
    n2=int(numberTwoStringVar.get())
    total=n1+n2
    user = int(answerEntryStringVar.get())
    if user == total:
        resultStringVar.set(f"{total} True")
    else:
        resultStringVar.set(f"{total} False")






#main
#create holding frames
root = Tk()
mainframe = Frame(root)
questionFrame = Frame(mainframe)

#Create widgets
numberOneStringVar = StringVar()
numberOneLabel = Label(questionFrame, text="", font=("Arial", 50), textvariable = numberOneStringVar)

numberTwoStringVar = StringVar()
numberTwoLabel = Label(questionFrame, text="", font=("Arial", 50), textvariable = numberTwoStringVar)

operationLabel = Label(questionFrame, text="+", font=("Arial", 50))

questionButton = Button(mainframe, text="???", font=("Arial", 20), command=getNewQuestion)
answerButton = Button(mainframe, text="check", font=("Arial", 20), command=checkAnswer)

answerEntryStringVar = StringVar()
answerEntry = Entry(mainframe, font=("Arial", 50),textvariable=answerEntryStringVar, width=5)

resultStringVar = StringVar()
resultLabel = Label(mainframe, text="", font=("Arial", 30), textvariable=resultStringVar)

#Grid the widgets
##############
root.minsize(width=400, height=400)
root.maxsize(width=600, height=400)

mainframe.grid(padx=100, pady=100)
questionFrame.grid(row=1, column=1, columnspan=2)

numberOneLabel.grid(row=1, column=1)
operationLabel.grid(row=1, column=2)
numberTwoLabel.grid(row=1, column=3)

questionButton.grid(row=2, column=1, ipadx = 20)
answerButton.grid(row=2, column=2, ipadx=20)

answerEntry.grid(row=3, column=1, columnspan=2)

resultLabel.grid(row=4, column=1, columnspan=2)


root.mainloop()
