<<<<<<< HEAD
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
        strTemp = '=========================\n'
        if disflag == 0:
            strTemp += "   学号       姓名\n"
            for (id, name, addr) in self.stuList:
                strTemp += "{: ^10}  {: ^6}\n".format(id, name)
        elif disflag == 1:
            strTemp += "   学号       姓名        物理地址\n"
            for (id, name, addr) in self.stuList:
                strTemp += "{: ^10}  {: ^6}  {: >19}\n".format(id, name, addr)
        return strTemp+"=========================\n"

    def createList(self, located_list, grade, profession, classNo):
        """创建学生列表"""
        self.grade = grade
        self.profession = profession
        self.classNo = classNo
        self.filename = "save\\{}级{}{}班学生名单".format(grade, profession, classNo)
        for student in located_list:
            if student not in self.stuList:
                self.stuList.append(student)
        return str("{}级{}{}班学生名单创建完毕\n".format(grade, profession, classNo))

    def addStu(self, id, name, addr="Null"):
        """添加学生"""
        strTemp = ''
        self.stuList.append([id, name, addr])
        strTemp += "已将{},{},{}加入列表.\n".format(id, name, addr)
        return strTemp

    def delStu(self, idD, nameD="Null", addrD="Null"):
        """删除学生（至少输入目标学号）"""
        strTemp = ''
        for (id, name, addr) in self.stuList:
            if (id == idD or name == nameD or addr == addrD):
                self.stuList.remove([id, name, addr])
                strTemp += "已将{},{},{}删除.\n".format(id, name, addr)
                return strTemp

    def checkAddr(self, located_list):
        """将实时列表与存储列表进行比较并列出可疑设备"""
        strTemp = ''
        suspDevices = []
        for (idT, nameT, addrT) in located_list:
            for (id, name, addr) in self.stuList:
                if (id == idT and name == nameT and addr != addrT):
                    suspDevices.append((idT, nameT, addrT))
        if len(suspDevices) == 0:
            strTemp += "没有疑似更换设备的学生签到.\n"
            return strTemp
        else:
            strTemp += "疑似更换设备的学生有：\n"
            for (id, name, addr) in suspDevices:
                strTemp += "{} ".format(name)
            strTemp += "\n若出现误判请向老师展示你的物理地址\n"
        return strTemp

    def checkList(self, located_list):
        """通过学生列表进行签到统计并列出缺席学生"""
        strTemp = ''
        self.absentStu = []
        for stu in self.stuList:
            if stu not in located_list:
                self.absentStu.append(stu)
                strTemp += "{}未签到！\n".format(stu)
        strTemp += "\n"
        strTemp += "{}级{}{}班应到{}人，实到{}人，缺席{}人\n".format(
            self.grade, self.profession, self.classNo, len(self.stuList),
            len(self.stuList) - len(self.absentStu), len(self.absentStu))
        if len(self.absentStu) == 0:
            return strTemp
        else:
            strTemp += "缺席学生有：\n"
            for (id, name, addr) in self.absentStu:
                strTemp += "{},{}\n".format(id, name)
            return strTemp

    def saveList(self):
        """保存学生信息列表"""
        with open("{}.json".format(self.filename), 'w',
                  encoding='utf-8') as file_obj:
            json.dump(self.stuList, file_obj)
        return "学生信息列表保存完毕\n"

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
            return str("sorry,file not found!")
        else:
            self.stuList = lines
            return str("{}级{}{}班学生名单加载完毕.\n".format(grade, profession, classNo))


if __name__ == '__main__':
    print("该模块不能被独立运行！")
=======
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
        strTemp = '=========================\n'
        if disflag == 0:
            strTemp += "   学号       姓名\n"
            for (id, name, addr) in self.stuList:
                strTemp += "{: ^10}  {: ^6}\n".format(id, name)
        elif disflag == 1:
            strTemp += "   学号       姓名        物理地址\n"
            for (id, name, addr) in self.stuList:
                strTemp += "{: ^10}  {: ^6}  {: >19}\n".format(id, name, addr)
        return strTemp+"=========================\n"

    def createList(self, located_list, grade, profession, classNo):
        """创建学生列表"""
        self.grade = grade
        self.profession = profession
        self.classNo = classNo
        self.filename = "save\\{}级{}{}班学生名单".format(grade, profession, classNo)
        for student in located_list:
            if student not in self.stuList:
                self.stuList.append(student)
        return str("{}级{}{}班学生名单创建完毕\n".format(grade, profession, classNo))

    def addStu(self, id, name, addr="Null"):
        """添加学生"""
        strTemp = ''
        self.stuList.append([id, name, addr])
        strTemp += "已将{},{},{}加入列表.\n".format(id, name, addr)
        return strTemp

    def delStu(self, idD, nameD="Null", addrD="Null"):
        """删除学生（至少输入目标学号）"""
        strTemp = ''
        for (id, name, addr) in self.stuList:
            if (id == idD or name == nameD or addr == addrD):
                self.stuList.remove([id, name, addr])
                strTemp += "已将{},{},{}删除.\n".format(id, name, addr)
                return strTemp

    def checkAddr(self, located_list):
        """将实时列表与存储列表进行比较并列出可疑设备"""
        strTemp = ''
        suspDevices = []
        for (idT, nameT, addrT) in located_list:
            for (id, name, addr) in self.stuList:
                if (id == idT and name == nameT and addr != addrT):
                    suspDevices.append((idT, nameT, addrT))
        if len(suspDevices) == 0:
            strTemp += "没有疑似更换设备的学生签到.\n"
            return strTemp
        else:
            strTemp += "疑似更换设备的学生有：\n"
            for (id, name, addr) in suspDevices:
                strTemp += "{} ".format(name)
            strTemp += "\n若出现误判请向老师展示你的物理地址\n"
        return strTemp

    def checkList(self, located_list):
        """通过学生列表进行签到统计并列出缺席学生"""
        strTemp = ''
        self.absentStu = []
        for stu in self.stuList:
            if stu not in located_list:
                self.absentStu.append(stu)
                strTemp += "{}未签到！\n".format(stu)
        strTemp += "\n"
        strTemp += "{}级{}{}班应到{}人，实到{}人，缺席{}人\n".format(
            self.grade, self.profession, self.classNo, len(self.stuList),
            len(self.stuList) - len(self.absentStu), len(self.absentStu))
        if len(self.absentStu) == 0:
            return strTemp
        else:
            strTemp += "缺席学生有：\n"
            for (id, name, addr) in self.absentStu:
                strTemp += "{},{}\n".format(id, name)
            return strTemp

    def saveList(self):
        """保存学生信息列表"""
        with open("{}.json".format(self.filename), 'w',
                  encoding='utf-8') as file_obj:
            json.dump(self.stuList, file_obj)
        return "学生信息列表保存完毕\n"

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
            return str("sorry,file not found!")
        else:
            self.stuList = lines
            return str("{}级{}{}班学生名单加载完毕.\n".format(grade, profession, classNo))


if __name__ == '__main__':
    print("该模块不能被独立运行！")
>>>>>>> b4a4d6bfd4510d0b2e5d40ba39e5f9302901ad10
