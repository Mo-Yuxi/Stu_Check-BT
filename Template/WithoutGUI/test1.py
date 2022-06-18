import tkinter as tk


def printentry():
    print(var.get())


root = tk.Tk()
var = tk.StringVar()
tk.Entry(root, textvariable=var).pack()  # 设置输入框对应的文本变量为var
tk.Button(root, text="print entry", command=printentry).pack()

root.mainloop()

#自定义的线程函数类
def thread_it(func, *args):
  '''将函数放入线程中执行'''
  # 创建线程
  t = threading.Thread(target=func, args=args) 
  # 守护线程
  t.setDaemon(True) 
  # 启动线程
  t.start()
 
按钮绑定函数的写法：
bt_test=tk.Button(window,text='测试',command=lambda :thread_it(test_def))