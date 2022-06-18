import bluetooth
import tkinter
import threading
from tkinter import scrolledtext
from model_studentlist_tk_v031 import StudentList


# 自定义的线程函数类
def thread_it(func, *args):
    '''将函数放入线程中执行'''
    # 创建线程
    t = threading.Thread(target=func, args=args)
    # 守护线程
    t.setDaemon(True)
    # 启动线程
    t.start()


stu1 = StudentList()

window = tkinter.Tk()
window.geometry('600x400')
window.resizable(False, False)
window.title('蓝牙学生点名系统v0.3.1    Designed By 2019级物联网工程开源大帝组')

grade_input = tkinter.StringVar()
profession_input = tkinter.StringVar()
classNo_input = tkinter.StringVar()
testout1 = tkinter.StringVar()

located_list = []
grade = -1
profession = ''
classNo = -1
id = -1
name = ''
addr = 'Null'


def One():
    if (len(located_list) == 0):
        Entry_out.insert('end', "列表不存在, 请先进行扫描。\n")
        Entry_out.see('end')
    elif (grade_input.get() == '' or profession_input.get() == ''
            or classNo_input.get() == ''):
        Entry_out.insert('end', "请先输入正确的信息创建学生名单。\n")
        Entry_out.see('end')
    else:
        grade = grade_input.get()
        profession = profession_input.get()
        classNo = classNo_input.get()
        strReturn = stu1.createList(located_list, grade, profession, classNo)
        Entry_out.insert('end', strReturn)
        Entry_out.see('end')


def Two():
    if (stu1.grade != -1 or stu1.classNo != -1):
        strReturn = stu1.showList()
        Entry_out.insert('end', strReturn)
        Entry_out.see('end')
    else:
        Entry_out.insert('end', "学生名单不存在，请先加载或创建学生名单。\n")
        Entry_out.see('end')


def Three():
    if (stu1.grade == -1 or stu1.classNo == -1):
        Entry_out.insert('end', "学生名单不存在，请先加载或创建学生名单。\n")
        Entry_out.see('end')
    elif (grade_input.get() == '' or profession_input.get() == ''):
        Entry_out.insert('end', "请先输入正确的信息以添加学生。\n")
        Entry_out.see('end')
    else:
        name = grade_input.get()
        id = profession_input.get()
        addr = classNo_input.get()
        strReturn = stu1.addStu(id, name, addr)
        Entry_out.insert('end', strReturn)
        Entry_out.see('end')


def Four():
    if (stu1.grade == -1 or stu1.classNo == -1):
        Entry_out.insert('end', "学生名单不存在，请先加载或创建学生名单。\n")
        Entry_out.see('end')
    elif (grade_input.get() == '' or profession_input.get() == ''
            or classNo_input.get() == ''):
        Entry_out.insert('end', "请先输入正确的信息以删除学生。\n")
        Entry_out.see('end')
    else:
        name = grade_input.get()
        id = profession_input.get()
        addr = classNo_input.get()
        strReturn = stu1.delStu(id, name, addr)
        Entry_out.insert('end', strReturn)
        Entry_out.see('end')


def Five():
    strReturn = ''
    if (stu1.grade != -1 or stu1.classNo != -1):
        if len(located_list) != 0:
            strReturn += stu1.checkList(located_list)
            strReturn += stu1.checkAddr(located_list)
            Entry_out.insert('end', strReturn)
            Entry_out.see('end')
        else:
            Entry_out.insert('end', "列表不存在, 请先加载列表或进行扫描。\n")
            Entry_out.see('end')
    else:
        Entry_out.insert('end', "学生名单不存在，请先加载或创建学生名单。\n")
        Entry_out.see('end')


def Six():
    strReturn = ''
    if len(stu1.stuList) != 0:
        strReturn = stu1.saveList()
        Entry_out.insert('end', strReturn)
        Entry_out.see('end')
    else:
        Entry_out.insert('end', "学生名单不存在，请先加载或创建学生名单。\n")
        Entry_out.see('end')


def Seven():
    strReturn = ''
    strReturn = stu1.loadList()
    if (strReturn == "fileERR\n"):
        stu1.grade = -1
        stu1.profession = 'Null'
        stu1.classNo = -1
    strReturn += '\n'
    Entry_out.insert('end', strReturn)
    Entry_out.see('end')


def Scan():
    Entry_out.insert('end', "扫描中, 请等待10s...\n")
    Entry_out.see('end')
    devices_list = bluetooth.discover_devices(lookup_names=True)
    lenTemp = len(located_list)
    if lenTemp == 0:
        for (addr1, name1) in devices_list:
            if("#1#." in name1):
                addTemp = [name1[4:14], name1[14:], addr1]
                located_list.append(addTemp)
    elif lenTemp != 0:
        if lenTemp > len(devices_list):
            for (addr1, name1) in devices_list:
                for Located in located_list:
                    if addr1 == Located[2]:
                        located_list.remove(Located)
        if lenTemp <= len(devices_list):
            for Located in located_list:
                for (addr1, name1) in devices_list:
                    if addr1 == Located[2]:
                        located_list.remove(Located)
        for (addr1, name1) in devices_list:
            if("#1#." in name1):
                addTemp = [name1[4:14], name1[14:], addr1]
                located_list.append(addTemp)
    Entry_out.insert('end', "扫描完成\n\n")
    Entry_out.see('end')


Entry_grade = tkinter.Entry(window, textvariable=grade_input)
Entry_grade.place(x=100, y=160, width=100, height=20)
Entry_prof = tkinter.Entry(window, textvariable=profession_input)
Entry_prof.place(x=100, y=220, width=100, height=20)
Entry_class = tkinter.Entry(window, textvariable=classNo_input)
Entry_class.place(x=100, y=280, width=100, height=20)
Entry_out = scrolledtext.ScrolledText(window, width=40, height=27)
Entry_out.place(x=300, y=20)
bott_getin = tkinter.Button(window, text="扫描", command=lambda: thread_it(Scan))
bott_getin.place(x=30, y=40, width=60, height=30)
bott_getin = tkinter.Button(window, text="创建名单", command=One)
bott_getin.place(x=130, y=40, width=60, height=30)
bott_getin = tkinter.Button(window, text="显示名单", command=Two)
bott_getin.place(x=230, y=40, width=60, height=30)
bott_getin = tkinter.Button(window, text="添加学生", command=Three)
bott_getin.place(x=30, y=80, width=60, height=30)
bott_getin = tkinter.Button(window, text="删除学生", command=Four)
bott_getin.place(x=130, y=80, width=60, height=30)
bott_getin = tkinter.Button(window, text="签到", command=Five)
bott_getin.place(x=230, y=80, width=60, height=30)
bott_getin = tkinter.Button(window, text="保存名单", command=Six)
bott_getin.place(x=60, y=330, width=80, height=35)
bott_getin = tkinter.Button(window, text="加载名单", command=Seven)
bott_getin.place(x=170, y=330, width=80, height=35)

Label1 = tkinter.Label(window, text='年级/姓名:')
Label1.place(x=100, y=140)
Label1 = tkinter.Label(window, text='专业/学号:')
Label1.place(x=100, y=200)
Label1 = tkinter.Label(window, text='班级/地址:')
Label1.place(x=100, y=260)

window.mainloop()
