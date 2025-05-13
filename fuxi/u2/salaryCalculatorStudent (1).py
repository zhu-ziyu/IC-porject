from tkinter import *


    
def calculatePayment():
    annual = dollarVar.get()
    # 2) 取各项扣款比例
    tax_rate    = taxVar.get()
    rrsp_rate   = rrspVar.get()
    union_rate  = unionVar.get()
    health_rate = healthVar.get()
    # 3) 总扣款比例
    total_deduction = tax_rate + rrsp_rate + union_rate + health_rate
    # 4) 扣款后的净年薪
    net_annual = annual * (1 - total_deduction)
    # 5) 从 Spinbox 里取周期数（"52 - weekly" 取前面的数字）
    periods = int(freqVar.get())
    # 6) 计算每期收入
    per_pay = net_annual / periods
    # 7) 更新界面上的两个 Label
    paymentVar.set(f"${per_pay:,.2f}/pmt")
    yearVar   .set(f"${annual:,}")


#MAIN
root = Tk()
mainframe = Frame(root)

#Create widgets

titleLabel = Label(mainframe, text="Salary Calculator", font=("Arial", 50))

dollarVar = IntVar()
dollarVar.set(45000)
dollarScale = Scale(mainframe, from_=100000, to=20000, orient=VERTICAL, width=50, length=300, resolution=5000, variable=dollarVar)

frequencies = ["52 - weekly", "24 - bimonthly", "12 - monthly"]
freqVar = StringVar()
freqSpinbox = Spinbox(mainframe, textvariable=freqVar, values=frequencies)


deductFrame = LabelFrame(mainframe, text="Deductions")
taxVar = DoubleVar()
taxCheck = Checkbutton(deductFrame, text="Tax", variable=taxVar, onvalue=0.35, offvalue =0)
rrspVar = DoubleVar()
rrspCheck = Checkbutton(deductFrame, text="RRSP", variable=rrspVar, onvalue=0.13, offvalue=0)
unionVar = DoubleVar()
unionCheck = Checkbutton(deductFrame, text="Union Dues", variable=unionVar, onvalue=0.01, offvalue=0)
healthVar = DoubleVar()
healthCheck = Checkbutton(deductFrame, text="Health Plan", variable=healthVar, onvalue=0.025, offvalue=0)



paymentVar = StringVar()
paymentLabel = Label(mainframe, textvariable=paymentVar, font=("Arial, 30"))

yearVar = StringVar()
yearLabel = Label(mainframe, textvariable=yearVar, font=("Arial, 15"))


calculateButton = Button(mainframe, text="each paycheck?", command=calculatePayment)

#Grid widgets
mainframe.grid(padx=50, pady=50)

titleLabel.grid(row=0, column=1, columnspan=2, pady=20, sticky=E)
dollarScale.grid(row=1, column=1, rowspan=5)
freqSpinbox.grid(row=1, column=2, padx=30, sticky=E+W)
yearLabel.grid(row=2, column=1, padx=30, sticky=E+W)
deductFrame.grid(row=2, column=2, padx=30, ipadx=50, sticky=N)
taxCheck.grid(sticky=W)
rrspCheck.grid(sticky=W)
unionCheck.grid(sticky=W)
healthCheck.grid(sticky=W)
paymentLabel.grid(row=3, column=1, columnspan=2, pady=20, sticky=E)

calculateButton.grid(row=3, column=2, ipady=15, pady=10, padx=30, sticky=E+W)

paymentLabel.grid(row=4, column=2)
yearLabel.grid(row=5, column=2)


##titleLabel.grid()
##dollarScale.grid()
##freqSpinbox.grid()
##
##deductFrame.grid()
##taxCheck.grid()
##rrspCheck.grid()
##unionCheck.grid()
##healthCheck.grid()
##
##
##calculateButton.grid()
##
##paymentLabel.grid()
##yearLabel.grid()


root.mainloop()


