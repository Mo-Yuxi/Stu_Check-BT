import json
from tkinter import filedialog


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
        self.filename = ""
        # self.filename = "save\\{}级{}{}班学生名单".format(grade, profession, classNo)

    def showList(self, disflag=0) -> None:
        """显示学生列表(model:是否显示硬件地址)"""
        strTemp = '============================\n'
        if disflag == 0:
            strTemp += "   学号       姓名\n"
            for (id, name, addr) in self.stuList:
                strTemp += "{: ^10}  {: ^6}\n".format(id, name)
        elif disflag == 1:
            strTemp += "   学号       姓名        物理地址\n"
            for (id, name, addr) in self.stuList:
                strTemp += "{: ^10}  {: ^6}  {: >19}\n".format(id, name, addr)
        return strTemp + "============================\n"

    def createList(self, located_list, grade, profession, classNo):
        """创建学生列表"""
        self.grade = grade
        self.profession = profession
        self.classNo = classNo
        self.filename = "save\\{}级{}{}班学生名单".format(grade, profession, classNo)
        stuTemp = len(self.stuList)
        if stuTemp >= len(located_list):
            for Located in located_list:
                for student in self.stuList:
                    if Located[2] == student[2]:
                        self.stuList.remove(student)
        if stuTemp < len(located_list):
            for student in self.stuList:
                for Located in located_list:
                    if Located[2] == student[2]:
                        self.stuList.remove(student)
        for addTemp in located_list:
            self.stuList.append(addTemp)
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
        delflag = 0
        for (id, name, addr) in self.stuList:
            if (id == idD or name == nameD or addr == addrD):
                self.stuList.remove([id, name, addr])
                delflag = 1
                strTemp += "已将{},{},{}删除.\n".format(id, name, addr)
                return strTemp
        if delflag == 0:
            return str("没有查询到目标学生, 删除失败.\n")

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
            for stuLocated in located_list:
                if stu[1] != stuLocated[1]:
                    self.absentStu.append(stu)
                    strTemp += "{}未签到！\n".format(stu[1])
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
        saveTemp = {
            'classNo': self.classNo,
            'grade': self.grade,
            'profession': self.profession,
            'list': self.stuList
        }
        self.filename = filedialog.asksaveasfilename(title='保存学生名单',
                                                     filetypes=[('json',
                                                                 '*.json')],
                                                     defaultextension='.json')
        with open("{}".format(self.filename), 'w',
                  encoding='utf-8') as file_obj:
            json.dump(saveTemp, file_obj)
        return "学生信息列表保存完毕\n"

    def loadList(self):
        """从文件加载学生信息列表"""
        self.filename = filedialog.askopenfilename(title='加载学生名单',
                                                   filetypes=[('json',
                                                               '*.json')])
        with open(
                "{}".format(self.filename),
                'r',
        ) as file_obj:
            loadTemp = json.load(file_obj)
            try:
                self.stuList = loadTemp['list']
                self.grade = loadTemp['grade']
                self.profession = loadTemp['profession']
                self.classNo = loadTemp['classNo']
                # self.filename = "save\\{}级{}{}班学生名单".format(
                #     self.grade, self.profession, self.classNo)
                return str("{}级{}{}班学生名单加载完毕.\n".format(
                    self.grade, self.profession, self.classNo))
            except Exception:
                return str("文件错误！\n")


if __name__ == '__main__':
    print("该模块不能被独立运行！")
