from tkinter import *
from tkinter import messagebox

def volume_changed(value=None):
    """
    当滑块值改变时调用：检查临界值，弹出消息框，并更新槽颜色
    参数 value 是 Scale 的回调（可以忽略）
    """
    vol = volume_var.get()
    # a) 当达到最大 100，弹出警告
    if vol == 100:
        messagebox.showwarning("Warning", "Volume at maximum!")
    #    当达到最小 0，弹出信息
    elif vol == 0:
        messagebox.showinfo("Info", "Volume muted!")
    # 更新槽的颜色
    update_trough_color()

def update_trough_color():
    """
    b) 根据当前音量修改 Scale 的 troughcolor
      80+   => 红色 #CC6666
      20-   => 蓝色 #6699CC
      其它  => 黄褐 #CC9966
    """
    vol   = volume_var.get()
    if vol >= 80:
        color = "#CC6666"
    elif vol <= 20:
        color = "#6699CC"
    else:
        color = "#CC9966"
    volume_scale.config(troughcolor=color)

def increase_volume(event=None):
    """
    c) 音量加一，不能超过 100，然后触发 volume_changed
    """
    vol = volume_var.get()
    if vol < 100:
        volume_var.set(vol + 1)
        volume_changed()

def decrease_volume(event=None):
    """
    c) 音量减一，不能低于 0，然后触发 volume_changed
    """
    vol = volume_var.get()
    if vol > 0:
        volume_var.set(vol - 1)
        volume_changed()

# —— 主程序 ——
root = Tk()
root.title("Volume Warning")

mainframe = Frame(root)
mainframe.grid(padx=50, pady=50)

# 绑定音量变量
volume_var = IntVar(value=50)

# 创建垂直 Scale，并把 command 绑定到 volume_changed
volume_scale = Scale(
    mainframe,
    variable=volume_var,
    from_=100, to=0,
    length=300, width=80,
    orient=VERTICAL,
    troughcolor='#CC9966',
    command=volume_changed
)
volume_scale.grid(row=1, column=1, padx=20, pady=20)

# 绑定键盘上下键到增减函数
root.bind("<Up>",   increase_volume)
root.bind("<Down>", decrease_volume)

root.mainloop()
