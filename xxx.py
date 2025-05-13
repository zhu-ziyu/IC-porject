import random
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

# 假设有若干地震效果文字写在列表里
earthquake_info = [
    "Magnitude 1: 感觉不到",
    "Magnitude 2: 微振",
    "Magnitude 3: 明显振动",
    "Magnitude 4: 家具晃动",
    "Magnitude 5: 室内物品掉落"
]

def change_earthquake_info(idx):
    display_var.set(earthquake_info[idx])

def show_error():
    messagebox.showerror('Earthquake Information',
                         'Function not available at this time')

def show_warning():
    messagebox.showwarning('Earthquake Information',
                           'Choose a value on the scale')

def show_info():
    messagebox.showinfo('Earthquake Information',
                        'Visualization of earthquake effect')

def ask_example():
    user_answer = messagebox.askyesno(
        'Earthquake Information',
        "Use the scale to see the effects.\nWould you like an example?"
    )
    if user_answer:
        idx = random.randint(0, len(earthquake_info)-1)
        change_earthquake_info(idx)

# 主程序
root = Tk()
root.title("Earthquake Simulator")

font_small  = Font(size=12)
font_medium = Font(size=16)

# 显示地震描述
display_var = StringVar(value="请选择震级")
display_label = Label(root, textvariable=display_var, font=font_medium)
display_label.pack(pady=10)

# 模拟一个调节地震强度的 Scale
scale_var = IntVar(value=0)
scale = Scale(root, from_=0, to=len(earthquake_info)-1,
              orient=HORIZONTAL, variable=scale_var,
              command=lambda v: change_earthquake_info(int(v)))
scale.pack(fill=X, padx=20)

# 弹窗按钮组
btn_frame = Frame(root)
btn_frame.pack(pady=10)

Button(btn_frame, text="Error",   command=show_error).grid(row=0, column=0, padx=5)
Button(btn_frame, text="Warning", command=show_warning).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Info",    command=show_info).grid(row=0, column=2, padx=5)
Button(btn_frame, text="Example?",command=ask_example).grid(row=0, column=3, padx=5)

root.mainloop()
