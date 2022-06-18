import bluetooth
from model_studentlist_cmd import StudentList

stu1 = StudentList()
input("请按下回车开始扫描周围学生设备...")
print("扫描中，请稍后...")
located_list = []
devices_list = bluetooth.discover_devices(lookup_names=True)
for (addr, name) in devices_list:
    if ("#1#." in name and addr not in located_list):
        addTemp = [name[4:14], name[14:], addr]
        located_list.append(addTemp)
print("扫描完毕...")
mainInterface = """
=======================================
                主菜单
    1.创建学生名单
    2.显示学生名单
    3.添加学生
    4.删除学生
    5.学生签到
    6.保存学生名单
    7.加载学生名单
    8.退出
---------------------------------------
Powered By 物联网工程短距x组
=======================================
"""
powerOn = 1
mode = -1
while (powerOn == 1):
    print(mainInterface)
    mode = input("请选择模式：")
    while (mode == '' or mode > "8" or mode < "1"):
        mode = input("请选择模式：")
    mode = int(mode)
    if mode == 1:
        grade = input("请设定年级：")
        profession = input("请设定专业：")
        classNo = input("请设定班级号：")
        stu1.createList(located_list, grade, profession, classNo)
        print("{}级{}{}班名单已创建完毕\n".format(grade, profession, classNo))
    elif mode == 7:
        grade = input("请输入年级：")
        profession = input("请输入专业：")
        classNo = input("请输入班级号：")
        stu1.loadList(grade, profession, classNo)
        print("{}级{}{}班名单已加载完毕\n".format(grade, profession, classNo))
    elif mode == 8:
        print("感谢使用.")
        powerOn = 0
    elif (mode > 1 and mode < 7):
        if stu1.classNo == -1:
            print("学生名单未导入，请创建或加载学生列表")
        else:
            if mode == 2:
                stu1.showList()
            elif mode == 3:
                idA = input("请输入学号：")
                nameA = input("请输入名字：")
                addrA = input("请输入硬件地址：")
                stu1.addStu(idA, nameA, addrA)
                print("已将学生{},{}添加至学生列表.\n".format(idA, nameA))
            elif mode == 4:
                idA = input("请输入学号：")
                stu1.delStu(idA)
                print("已将学生{}删除\n".format(idA))
            elif mode == 5:
                stu1.checkList(located_list)
                stu1.checkAddr(located_list)
            elif mode == 6:
                stu1.saveList()
                print("\n")
