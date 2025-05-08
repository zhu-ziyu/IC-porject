from tkinter import *
from tkinter.font import Font

def change_weather(value):

    idx = int(value)
    if idx == 1:      # Rain
        img = rain_photo
        col = '#6D6D6D'
    elif idx == 2:    # Cloud
        img = cloud_photo
        col = '#83D4ED'
    elif idx == 3:    # Sun + Cloud
        img = suncloud_photo
        col = '#C4E1E9'
    else:             # idx == 4, Sun
        img = sun_photo
        col = '#FBD462'

    # 更新天气图标和背景色
    weather_image_label.config(image=img, bg=col)


    # 把整个窗口／主框架也染成同色
    root.config(bg=col)
    mainframe.config(bg=col)

    # 更新滑块的槽和背景
    weather_scale.config(
        bg=col,
        troughcolor=col,
        highlightbackground=col
    )


# === 主程序 ===
root = Tk()
root.title("Weather Slider")

mainframe = Frame(root)
mainframe.grid(padx=100, pady=50)


# 预加载四张图片
sun_photo      = PhotoImage(file="sunny.png")
suncloud_photo = PhotoImage(file="suncloud.png")
cloud_photo    = PhotoImage(file="cloudy.png")
rain_photo     = PhotoImage(file="rainy.png")

# 用于显示天气图标
weather_image_label = Label(mainframe, image=None)
weather_image_label.grid(row=1, column=1, pady=20)

# 滑块设置，从 1 到 4，对应上面4种天气
weather_var = IntVar(value=1)
weather_scale = Scale(
    mainframe,
    from_=1,
    to=4,
    variable=weather_var,
    label="Weather",
    width=30,
    length=200,
    showvalue=False,
    orient=HORIZONTAL,
    troughcolor='#6D6D6D',      # 初始槽色
    bg='#6D6D6D',               # 初始背景
    highlightbackground='#6D6D6D',
    command=change_weather
)
weather_scale.grid(row=2, column=1, ipadx=50)

# 启动时先调用一次，显示初始状态
change_weather(weather_var.get())

root.mainloop()
