import tkinter
from tkinter import messagebox
import re

tk = tkinter.Tk()
tk.geometry('300x210+500+200')
tk.resizable(False, False)
tk.title('计算器')

contentVar = tkinter.StringVar(tk, '')  # 自动刷新字符串变量，可用 set 和 get 方法进行传值和取值
contentEntry = tkinter.Entry(tk, textvariable=contentVar)  # 创建单行文本框
contentEntry['state'] = 'readonly'  # 设置文本框为只读
contentEntry.place(x=20, y=10, width=260, height=30)  # 设置文本框坐标及宽高

bvalue = [
    'C', '+', '-', '//', '2', '0', '1', '√', '3', '4', '5', '*', '6', '7', '8',
    '.', '9', '/', '**', '='
]
index = 0
for row in range(5):  # 将按钮进行 5x4 放置
    for col in range(4):
        d = bvalue[index]
        index += 1
        btnDigit = tkinter.Button(tk, text=d, command=lambda x=d: onclick(x))
        btnDigit.place(x=20 + col * 70, y=50 + row * 30, width=50, height=20)


def onclick(btn):
    operation = ('+', '-', '*', '/', '**', '//')  # 运算符
    content = contentVar.get()  # 获取文本框中的内容
    if content.startswith('.'):  # 如果已有内容是以小数点开头的，在前面加 0
        content = '0' + content  # 字符串可以直接用+来增加字符
    # 根据不同的按钮作出不同的反应
    if btn in '0123456789':  # 按下 0-9 在 content 中追加
        content += btn
    elif btn == '.':  # 将 content 从 +-*/ 这些字符的地方分割开来
        lastPart = re.split(r'\+|-|\*|/', content)[-1]
        if '.' in lastPart:  # 信息提示对话框
            messagebox.showerror('错误', '重复出现的小数点')
            return
        else:
            content += btn
    elif btn == 'C':
        content = ''  # 清除文本框
    elif btn == '=':
        try:
            content = str(eval(content))  # 对输入的表达式求值
        except Exception:
            messagebox.showerror('错误', '表达式有误')
            return
    elif btn in operation:
        if content.endswith(operation):
            messagebox.showerror('错误', '不允许存在连续运算符')
            return
        content += btn
    elif btn == '√':
        n = content.split('.')  # 从 . 处分割存入 n，n 是一个列表
        if all(map(lambda x: x.isdigit(), n)):  # 如果列表中所有的都是数字，就是为了检查表达式是不是正确的
            content = eval(content)**0.5
        else:
            messagebox.showerror('错误', '表达式错误')
            return
    contentVar.set(content)  # 将结果显示到文本框中


tk.mainloop()
