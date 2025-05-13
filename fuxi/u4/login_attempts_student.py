from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

# ——— 全局配置 ———
CORRECT_USER = "ADMIN"  # 正确用户名
CORRECT_PASS = "PASSWORD"  # 正确密码

attempts_left = 3  # 剩余尝试次数


# ——— 回调函数区 ———
def check_login():
    global attempts_left
    # 1）读取用户在 Entry 中输入的用户名和密码
    user = username_var.get().strip()
    pwd = password_var.get().strip()

    # 2）清空输入框（无论正确与否，都清空，让用户重新输入）
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    # 3）判断登录信息是否正确
    if user == CORRECT_USER and pwd == CORRECT_PASS:
        # 登录成功：弹出信息框提示欢迎
        messagebox.showinfo("Login Successful", "Welcome!")
        # （可选）禁用登录按钮，防止重复登录
        login_button.config(state=DISABLED)
    else:
        # 登录失败：剩余次数减 1
        attempts_left -= 1
        # 检查是否要冻结账号或剩余尝试次数提示
        check_freeze_account()


def check_freeze_account():
    global attempts_left
    # 如果还剩尝试次数，就告诉用户还有几次机会
    if attempts_left > 0:
        messagebox.showwarning(
            "Login Failed",
            f"Incorrect credentials.\nYou have {attempts_left} attempts left."
        )
    else:
        # 没有剩余次数：弹出冻结提示，并禁用登录按钮
        messagebox.showwarning(
            "Account Frozen",
            "No attempts left. Your account has been frozen."
        )
        login_button.config(state=DISABLED)


# ——— 主程序区 ———
root = Tk()
root.title("Login Attempts")

# 主框架
mainframe = Frame(root)
mainframe.grid(padx=50, pady=50)

# 字体
checkbook_big = Font(family='Checkbook', size=60)
checkbook_small = Font(family='Checkbook', size=20)

# 用户名标签 + 输入框
username_label = Label(mainframe, text="USERNAME:", font=checkbook_small)
username_var = StringVar()
username_entry = Entry(mainframe, textvariable=username_var,
                       width=10, font=checkbook_big)

# 密码标签 + 输入框（隐藏输入）
password_label = Label(mainframe, text="PASSWORD:", font=checkbook_small)
password_var = StringVar()
password_entry = Entry(mainframe, show="*", textvariable=password_var,
                       width=10, font=checkbook_big)

# 登录按钮，点击时调用 check_login
login_button = Button(mainframe, text="LOGIN",
                      command=check_login, font=checkbook_big)

# ——— 布局 ———
username_label.grid(row=1, column=1, sticky=E, padx=20, pady=20)
username_entry.grid(row=1, column=2, padx=20, pady=20)

password_label.grid(row=2, column=1, sticky=E, padx=20, pady=20)
password_entry.grid(row=2, column=2, padx=20, pady=20)

login_button.grid(row=3, column=2, padx=20, pady=(10, 0), sticky=EW)

root.mainloop()
