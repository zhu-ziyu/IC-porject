from tkinter import *
#头疼
def calculatePayment():

    salary = dollarVar.get()

    freq_str = freqVar.get()
    periods = int(freq_str.split()[0])



    total_ded = taxVar.get() + rrspVar.get() + unionVar.get() + healthVar.get()

    net_annual = salary * (1 - total_ded)

    pay = net_annual / periods

    paymentVar.set(f"${pay:,.2f}")
    yearVar.set(f"Annual after deductions: ${net_annual:,.2f}")


root = Tk()
root.title("Salary Calculator")

mainframe = Frame(root)
mainframe.grid(padx=50, pady=50)

titleLabel = Label(mainframe, text="Salary Calculator", font=("Arial", 50))
titleLabel.grid(row=0, column=1, columnspan=2, pady=20)


dollarVar = IntVar(value=45000)
dollarScale = Scale(
    mainframe,
    from_=100000,
    to=20000,
    orient=VERTICAL,
    width=50,
    length=300,
    resolution=5000,
    variable=dollarVar
)
dollarScale.grid(row=1, column=1, rowspan=5)

frequencies = ["52 - weekly", "24 - bimonthly", "12 - monthly"]
freqVar = StringVar(value=frequencies[0])
freqSpinbox = Spinbox(mainframe, textvariable=freqVar, values=frequencies)
freqSpinbox.grid(row=1, column=2, padx=30, sticky=E+W)


deductFrame = LabelFrame(mainframe, text="Deductions")
deductFrame.grid(row=2, column=2, padx=30, ipadx=50, sticky=N)

taxVar    = DoubleVar(value=0)
rrspVar   = DoubleVar(value=0)
unionVar  = DoubleVar(value=0)
healthVar = DoubleVar(value=0)

taxCheck    = Checkbutton(deductFrame, text="Tax",        variable=taxVar,    onvalue=0.35,  offvalue=0)
rrspCheck   = Checkbutton(deductFrame, text="RRSP",       variable=rrspVar,   onvalue=0.13,  offvalue=0)
unionCheck  = Checkbutton(deductFrame, text="Union Dues", variable=unionVar,  onvalue=0.01,  offvalue=0)
healthCheck = Checkbutton(deductFrame, text="Health Plan",variable=healthVar,onvalue=0.025, offvalue=0)

for cb in (taxCheck, rrspCheck, unionCheck, healthCheck):
    cb.pack(anchor=W)


calculateButton = Button(mainframe, text="Calculate Paycheck", command=calculatePayment)
calculateButton.grid(row=3, column=2, ipady=15, pady=10, padx=30, sticky=E+W)


paymentVar = StringVar()
paymentLabel = Label(mainframe, textvariable=paymentVar, font=("Arial", 30))
paymentLabel.grid(row=4, column=2)


yearVar = StringVar()
yearLabel = Label(mainframe, textvariable=yearVar, font=("Arial", 15))
yearLabel.grid(row=5, column=2)

root.mainloop()
