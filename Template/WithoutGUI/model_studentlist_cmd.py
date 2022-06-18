import json


class StudentList:
    """存储学生信息列表的类"""
    def __init__(self,
                 located_list=[],
                 classNo=-1,
                 grade=-1,
                 profession="Null") -> None:
        """初始化"""
        self.stuList = []
        self.absentStu = []
        self.locate_list = list(located_list)
        self.classNo = classNo
        self.grade = grade
        self.profession = profession
        self.filename = "save\\{}级{}{}班学生名单".format(grade, profession, classNo)

    def showList(self, disflag=0) -> None:
        """显示学生列表(model:是否显示硬件地址)"""
        if disflag == 0:
            print("---" * 8)
            print("   学号       姓名")
            for (id, name, addr) in self.stuList:
                print("{: ^10}  {: ^6}".format(id, name))
            print("---" * 8)
        elif disflag == 1:
            print("---" * 12)
            print("   学号       姓名        物理地址")
            for (id, name, addr) in self.stuList:
                print("{: ^10}  {: ^6}  {: >19}".format(id, name, addr))
            print("---" * 12)

    def createList(self, located_list, grade, profession, classNo):
        """创建学生列表"""
        self.grade = grade
        self.profession = profession
        self.classNo = classNo
        self.filename = "save\\{}级{}{}班学生名单".format(grade, profession, classNo)
        for student in located_list:
            if student not in self.stuList:
                self.stuList.append(student)

    def addStu(self, id, name, addr="Null"):
        """添加学生"""
        self.stuList.append((id, name, addr))
        print("已将{},{},{}加入列表.".format(id, name, addr))

    def delStu(self, idD, nameD="Null", addrD="Null"):
        """删除学生（至少输入目标学号）"""
        for (id, name, addr) in self.stuList:
            if (id == idD or name == nameD or addr == addrD):
                self.stuList.remove((id, name, addr))
                print("已将{},{},{}删除.".format(id, name, addr))

    def checkAddr(self, located_list):
        """将实时列表与存储列表进行比较并列出可疑设备"""
        suspDevices = []
        for (idT, nameT, addrT) in located_list:
            for (id, name, addr) in self.stuList:
                if (id == idT and name == nameT and addr != addrT):
                    suspDevices.append((idT, nameT, addrT))
        print("---" * 8)
        if len(suspDevices) == 0:
            print("没有疑似更换设备的学生签到.")
        else:
            print("疑似更换设备的学生有：")
            for (id, name, addr) in suspDevices:
                print(name, sep=" ")
            print("若出现误判请向老师展示你的物理地址")
        print("---" * 8)

    def checkList(self, located_list):
        """通过学生列表进行签到统计并列出缺席学生"""
        self.absentStu = []
        for stu in self.stuList:
            if stu not in located_list:
                self.absentStu.append(stu)
                print("{}未签到！".format(stu))
        print("\n")
        print("{}级{}{}班应到{}人，实到{}人，缺席{}人".format(
            self.grade, self.profession, self.classNo, len(self.stuList),
            len(self.stuList) - len(self.absentStu), len(self.absentStu)))
        if len(self.absentStu) != 0:
            print("缺席学生有：")
            for stu in self.absentStu:
                print("{},".format(stu))
        print("---" * 8)

    def saveList(self):
        """保存学生信息列表"""
        with open("{}.json".format(self.filename), 'w',
                  encoding='utf-8') as file_obj:
            json.dump(self.stuList, file_obj)

    def loadList(self, grade, profession, classNo):
        """从文件加载学生信息列表"""
        self.grade = grade
        self.profession = profession
        self.classNo = classNo
        self.filename = "save\\{}级{}{}班学生名单".format(grade, profession, classNo)
        try:
            with open(
                    "{}.json".format(self.filename),
                    'r',
            ) as file_obj:
                lines = json.load(file_obj)
        except FileNotFoundError:
            print("sorry,file not found!")
        else:
            self.stuList = lines


if __name__ == '__main__':
    print("该模块不能被独立运行！")
