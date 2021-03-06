<<<<<<< HEAD
# 基于蓝牙的学生点名器
本软件基于python开发，通过pybluez库调用系统蓝牙硬件扫描周围设备名，并通过记录特定规则的设备名来完成签到

### 已实现功能
  - [x] 通过周围蓝牙设备名称一键创建学生列表
  - [x] 蓝牙设备列表转换为学生列表
  - [x] 判断学生是否到场签到
  - [x] 判断学生是否为代签到
  - [x] 将学生列表保存到本地
  - [x] 从本地读取已保存的学生列表
  - [x] 添加、删除学生列表内的学生

#### 运行图
![image](https://raw.githubusercontents.com/Mo-Yuxi/Stu_Check-BT/main/img/run.png)

### 使用方法

#### 关于蓝牙设备名
+ 蓝牙名称格式：“#1#.”+“学号(10位)”+“姓名”
+ example: 2019211963墨雨汐："#1#.2019211963墨雨汐"

#### 首次使用/无学生列表文件
+ 确保蓝牙设备已开启
+ 启动软件后，等待学生启动蓝牙设备并修改蓝牙设备名，点击“扫描”按钮，等待扫描完毕
  + 若单次扫描无法覆盖全部学生则可多次更换设备位置并点击“扫描”按钮
+ 扫描完毕后，在下方文本框按提示输入教学班信息，再点击“创建名单”按钮
  + 若右侧信息窗口提示“x级x专业x班学生名单创建完毕”则表示名单创建成功
+ 可点击“显示名单”以显示当前学生列表
  + 此时可点击“保存名单”按钮将学生名单保存到本地文件中以便下次使用
+ 后续操作和 **已有学生列表文件** 的第四步开始的操作完全相同

#### 已有学生列表文件
+ 确保蓝牙设备已开启
+ 启动软件后点击“加载名单”按钮，在打开的窗口中打开以前导出的学生名单文件
+ 等待学生启动蓝牙设备并修改蓝牙设备名后，点击“扫描”按钮进行扫描，等待扫描完毕
+ 扫描完毕后，点击“签到按钮”，程序便会列举出缺勤情况列表与代签到列表


#### 关于python版本
+ 推荐 python3 (3.6-3.9)
**注：本程序基于 python 3.9.4 编写**

#### 关于UI
    程序图形化界面基于python自带的tkinter库开发

#### 关于pybluez库
##### 依赖库安装
`pip install pybluez`  
**注：pybluez库依赖于C++环境，在安装pybluez前请先确保电脑上已安装C++桌面开发环境，否则报错**  
**注：由于pybluez库已长时间无人更新  
      若电脑上安装的Microsoft Visual C++2015-2022 Redistributable较新  
      则直接install会出现错误，故请按照此方法创建文件link以使pip成功安装**  
https://blog.csdn.net/w12w12w12/article/details/116466157

#### 关于开源使用
  本项目基于GNU GPLv3协议进行开源

![image](https://camo.githubusercontent.com/db9cc5f2f01568952f34f4a58faf3198cd147d9f4a90db0918cd45484c3e544e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f5465636858756558692f5465636858756558692e737667)
=======
# 基于蓝牙的学生点名器
本软件基于python开发，通过pybluez库调用系统蓝牙硬件扫描周围设备名，并通过记录特定规则的设备名来完成签到

### 已实现功能
  - [x] 通过周围蓝牙设备名称一键创建学生列表
  - [x] 蓝牙设备列表转换为学生列表
  - [x] 判断学生是否到场签到
  - [x] 判断学生是否为代签到
  - [x] 将学生列表保存到本地
  - [x] 从本地读取已保存的学生列表
  - [x] 添加、删除学生列表内的学生

#### 运行图
![image](https://raw.githubusercontents.com/Mo-Yuxi/Stu_Check-BT/main/img/run.png)

### 使用方法

#### 关于蓝牙设备名
+ 蓝牙名称格式：“#1#.”+“学号(10位)”+“姓名”
+ example: 2019211963墨雨汐："#1#.2019211963墨雨汐"

#### 首次使用/无学生列表文件
+ 确保蓝牙设备已开启
+ 启动软件后，等待学生启动蓝牙设备并修改蓝牙设备名，点击“扫描”按钮，等待扫描完毕
  + 若单次扫描无法覆盖全部学生则可多次更换设备位置并点击“扫描”按钮
+ 扫描完毕后，在下方文本框按提示输入教学班信息，再点击“创建名单”按钮
  + 若右侧信息窗口提示“x级x专业x班学生名单创建完毕”则表示名单创建成功
+ 可点击“显示名单”以显示当前学生列表
  + 此时可点击“保存名单”按钮将学生名单保存到本地文件中以便下次使用
+ 后续操作和 **已有学生列表文件** 的第四步开始的操作完全相同

#### 已有学生列表文件
+ 确保蓝牙设备已开启
+ 启动软件后点击“加载名单”按钮，在打开的窗口中打开以前导出的学生名单文件
+ 等待学生启动蓝牙设备并修改蓝牙设备名后，点击“扫描”按钮进行扫描，等待扫描完毕
+ 扫描完毕后，点击“签到按钮”，程序便会列举出缺勤情况列表与代签到列表


#### 关于python版本
+ 推荐 python3 (3.6-3.9)
**注：本程序基于 python 3.9.4 编写**

#### 关于UI
    程序图形化界面基于python自带的tkinter库开发

#### 关于pybluez库
##### 依赖库安装
`pip install pybluez`  
**注：pybluez库依赖于C++环境，在安装pybluez前请先确保电脑上已安装C++桌面开发环境，否则报错**  
**注：由于pybluez库已长时间无人更新  
      若电脑上安装的Microsoft Visual C++2015-2022 Redistributable较新  
      则直接安装会出现错误，故请按照此方法创建文件link以使pip成功安装**  
https://blog.csdn.net/w12w12w12/article/details/116466157

#### 关于开源使用
  本项目基于GNU GPLv3协议进行开源

![image](https://raw.githubusercontents.com/Mo-Yuxi/Stu_Check-BT/main/img/GPL.png)
>>>>>>> b4a4d6bfd4510d0b2e5d40ba39e5f9302901ad10
