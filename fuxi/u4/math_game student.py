from tkinter import *
import random
from tkinter import messagebox

# 记录当前题目和正确答案
num1 = num2 = answer = 0
# 连续答对题目数
count_correct = 0

def get_new_question(low=1, high=10):
    """
    生成一条新的加法题目，默认从 1～10 取数。
    low/high 参数可用于更难的“加大问号”。
    """
    global num1, num2, answer
    # 随机取两个数
    num1 = random.randint(low, high)
    num2 = random.randint(low, high)
    answer = num1 + num2

    # 更新界面上的题目数字，清空 Entry 和结果标签
    number_one_string_var.set(str(num1))
    number_two_string_var.set(str(num2))
    answer_entry_string_var.set('')
    result_string_var.set('')

def show_answer(event):
    """
    a) 右键点击 Entry 时，弹出 info 对话框，给出答案。
    绑定到 answer_entry 的 <Button-3> 事件（Windows/Linux为右键）。
    """
    messagebox.showinfo("Answer", f"The answer is {answer}")

def check_answer():
    """
    b) 点击“check”按钮：
      - 如果 Entry 里没填，弹 warning 提醒
      - 否则判断对错，更新结果，并统计答对次数
      - 如果刚好答对 5 题，弹 question 对话框询问是否要做 bonus
    """
    global count_correct

    user_text = answer_entry_string_var.get().strip()
    # b) 如果没输入
    if user_text == "":
        messagebox.showwarning("Math Game", "You need to answer the question")
        return

    # 转成整数并判断
    try:
        user_answer = int(user_text)
    except ValueError:
        # 如果输入非数字，也当错
        result_string_var.set("INCORRECT")
        return

    if user_answer == answer:
        result_string_var.set("CORRECT")
        count_correct += 1
        # c) 如果答对满 5 题，弹出是否要做 Bonus 题
        if count_correct == 5:
            again = messagebox.askquestion(
                "Bonus Question",
                "Congrats! 5 correct.\nWould you like a bonus question?"
            )
            if again == 'yes':
                # 生成更难的题，比如 10～20 之间
                get_new_question(10, 20)
                return
    else:
        result_string_var.set("INCORRECT")

    # 正常生成下一题
    get_new_question()

# —— 界面搭建 ——
root = Tk()
root.title("Math Game")

mainframe = Frame(root, padx=50, pady=30)
mainframe.grid()

# 题目数字 + 加号
question_frame = Frame(mainframe)
question_frame.grid(row=1, column=1, columnspan=2)

number_one_string_var = StringVar()
number_one_label = Label(
    question_frame,
    textvariable=number_one_string_var,
    font=("Arial", 50)
)
number_one_label.grid(row=1, column=1)

operation_label = Label(
    question_frame,
    text="+",
    font=("Arial", 50)
)
operation_label.grid(row=1, column=2)

number_two_string_var = StringVar()
number_two_label = Label(
    question_frame,
    textvariable=number_two_string_var,
    font=("Arial", 50)
)
number_two_label.grid(row=1, column=3)

# “???” 按钮：生成新题
question_button = Button(
    mainframe,
    text="???",
    font=("Arial", 20),
    command=lambda: get_new_question()
)
question_button.grid(row=2, column=1, ipadx=20, ipady=10, sticky=E+W)

# “check” 按钮：检查答案
answer_button = Button(
    mainframe,
    text="check",
    font=("Arial", 20),
    command=check_answer
)
answer_button.grid(row=2, column=2, ipadx=10, ipady=10, sticky=E+W)

# 用户输入 Entry
answer_entry_string_var = StringVar()
answer_entry = Entry(
    mainframe,
    textvariable=answer_entry_string_var,
    font=("Arial", 50),
    width=5
)
answer_entry.grid(row=3, column=1, columnspan=2, sticky=E+W, pady=10)
# a) 绑定右键事件到 show_answer
answer_entry.bind("<Button-3>", show_answer)

# 显示“CORRECT/INCORRECT”
result_string_var = StringVar()
result_label = Label(
    mainframe,
    textvariable=result_string_var,
    font=("Arial", 30)
)
result_label.grid(row=4, column=1, columnspan=2)

# 首次启动时，生成一题
get_new_question()

root.mainloop()
