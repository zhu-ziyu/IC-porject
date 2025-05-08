from tkinter import *
from tkinter.font import Font

def updatePlan():

    idx = planChoiceVar.get()
    infoVar.set(planInformationList[idx])

root = Tk()
root.title("Spotify Plans")
root.config(bg="#1DB954")

mainframe = Frame(root, bg="#1DB954")
mainframe.grid(padx=50, pady=50)

smallFont = Font(family="Moonbeam", size=30)
largeFont = Font(family="Moonbeam", size=60)


planInformationList = [
    'INDIVIDUAL\n$9.99 CAD/mnth\n1 account',
    'DUO\n$12.99 CAD/mnth\n2 accounts',
    'FAMILY\n$14.99 CAD/mnth\n6 accounts',
    'STUDENT\n$4.99 CAD/mnth\n1 account'
]


planChoiceVar = IntVar(value=0)


options = ["individual", "duo", "family", "student"]
for col, name in enumerate(options):
    rb = Radiobutton(
        mainframe,
        text=name,
        variable=planChoiceVar,
        value=col,
        font=smallFont,
        command=updatePlan,
        bg="#1DB954",
        fg="white",
        selectcolor="#1DB954",
        activebackground="#1DB954",
        activeforeground="white",
        highlightthickness=0
    )
    rb.grid(row=0, column=col, padx=20)


infoVar = StringVar(value=planInformationList[0])
infoLabel = Label(
    mainframe,
    textvariable=infoVar,
    font=largeFont,
    bg="#1DB954",
    fg="black"
)
infoLabel.grid(row=1, column=0, columnspan=4, pady=30)

root.mainloop()
