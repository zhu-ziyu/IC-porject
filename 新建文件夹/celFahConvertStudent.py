from tkinter import *
from tkinter.font import Font

def updateAvailableConversions():
    in_scale = convertInVar.get()

    celciusOutRadio.config(state=NORMAL)
    fahrenheitOutRadio.config(state=NORMAL)
    kelvinOutRadio.config(state=NORMAL)

    if in_scale == "cel":
        celciusOutRadio.config(state=DISABLED)

        if convertOutVar.get() == "cel":
            convertOutVar.set("fah")
    elif in_scale == "fah":
        fahrenheitOutRadio.config(state=DISABLED)
        if convertOutVar.get() == "fah":
            convertOutVar.set("cel")
    else:
        kelvinOutRadio.config(state=DISABLED)
        if convertOutVar.get() == "kel":
            convertOutVar.set("cel")

def convertTemp():

    t_in = float(tempInVar.get())


    src = convertInVar.get()
    dst = convertOutVar.get()


    if src == "cel":
        c = t_in
    elif src == "fah":
        c = (t_in - 32) * 5/9
    else:
        c = t_in - 273.15


    if dst == "cel":
        result = c
    elif dst == "fah":
        result = c * 9/5 + 32
    else:
        result = c + 273.15


    tempOutVar.set(f'~{round(result)}°')



root = Tk()
root.title("Temperature Converter")

mainframe = Frame(root)
mainframe.grid(padx=100, pady=100)

# Fonts
smallF = Font(family="Mayflower Antique", size=20)
largeF = Font(family="Mayflower Antique", size=40)
xlargeF = Font(family="Mayflower Antique", size=80)

scaleInFrame = LabelFrame(mainframe, text="temperature in", font=smallF)
scaleInFrame.grid(row=2, column=1, rowspan=3, padx=50, sticky=N)

convertInVar = StringVar(value="fah")
for txt, val, r in [("celcius","cel",1), ("fahrenheit","fah",2), ("kelvin","kel",3)]:
    Radiobutton(
        scaleInFrame, text=txt, variable=convertInVar, value=val,
        font=largeF, command=updateAvailableConversions
    ).grid(row=r, sticky=W)


scaleOutFrame = LabelFrame(mainframe, text="temperature out", font=smallF)
scaleOutFrame.grid(row=2, column=3, rowspan=3, padx=50, sticky=N)

convertOutVar = StringVar(value="cel")
celciusOutRadio = Radiobutton(scaleOutFrame, text="celcius", variable=convertOutVar,
                              value="cel", font=largeF)
fahrenheitOutRadio = Radiobutton(scaleOutFrame, text="fahrenheit", variable=convertOutVar,
                                 value="fah", font=largeF)
kelvinOutRadio = Radiobutton(scaleOutFrame, text="kelvin", variable=convertOutVar,
                             value="kel", font=largeF)

celciusOutRadio.grid(row=1, sticky=W)
fahrenheitOutRadio.grid(row=2, sticky=W)
kelvinOutRadio.grid(row=3, sticky=W)


Label(mainframe, text="temp in?", font=smallF).grid(row=2, column=2, sticky=NW)

tempInVar = StringVar()
Entry(mainframe, textvariable=tempInVar, width=5, font=largeF)\
    .grid(row=3, column=2, pady=(0,30), sticky=EW)

Button(mainframe, text="convert", font=largeF, command=convertTemp)\
    .grid(row=4, column=2, sticky=EW)

tempOutVar = StringVar()
Label(mainframe, textvariable=tempOutVar, font=xlargeF).grid(row=5, column=2)

updateAvailableConversions()

root.mainloop()
