import tkinter as tk
import sys, os
import threading

from log import Log
from settings import add_settings
from run import f_run_b


root = tk.Tk()
file_name_format = None
Rd_b1_status = tk.IntVar()
Rd_b2_status = tk.IntVar()
Rd_b3_status = tk.IntVar()
Rd_b1_status.set(0)
Rd_b2_status.set(0)
Rd_b3_status.set(0)

def Rd_button_1():
    """文件备份选择1"""
    global file_name_format, Rd_b1_status
    file_name_format = 'disk'
    Log("U盘备份命名格式设置为U盘名称")
    Log("保存至配置文件中...")
    add_settings('f_name_format', file_name_format)
    Log("保存成功")
    Rd_b2_status.set(0)
    Rd_b3_status.set(0)

def Rd_button_2():
    """文件备份选择2"""
    global file_name_format, Rd_b2_status
    file_name_format = 'time'
    Log("U盘备份命名格式设置为时间")
    Log("保存至配置文件中...")
    add_settings('f_name_format', file_name_format)
    Log("保存成功")
    Rd_b1_status.set(0)
    Rd_b3_status.set(0)

def Rd_button_3():
    """文件备份选择3"""
    global file_name_format, Rd_b3_status
    file_name_format = 'both'
    Log("U盘备份命名格式设置为两者")
    Log("保存至配置文件中...")
    add_settings('f_name_format', file_name_format)
    Log("保存成功")
    Rd_b1_status.set(0)
    Rd_b2_status.set(0)

def Exit_button():
    """退出按钮"""
    Log("============程序关闭============")
    sys.exit()

def f_disk_button():
    """U盘选择"""
    with open('disk_choices.txt', 'w') as f:
        pass
    Log("创建U盘选择配置文件成功")
    os.system('notepad.exe disk_choices.txt')

def f_disk_right_button():
    """确认U盘选择"""
    try:
        with open('disk_choices.txt') as f:
            content = f.readlines()
        if (content[0] == 'all') or (content[0] == 'all\n'):
            add_settings('disk_choice', 'all')
            Log("保存U盘选择为全部成功")
        else:
            new_content = []
            # 处理U盘卷标字符
            for i in content:
                if '\n' in i:
                    temp_name = list(i)
                    del temp_name[-1]
                    temp_name = ''.join(temp_name)
                    new_content.append(temp_name)
                elif '\n' not in i:
                    new_content.append(i)
            content = new_content[:]
            del new_content
            add_settings('disk_choice', content)
            Log("保存U盘选择成功")
    except:
        pass

def f_file_format_button():
    """文件格式选择"""
    with open('file_format.txt', 'w') as f:
        pass
    Log("创建备份文件格式配置文件成功")
    os.system('notepad.exe file_format.txt')

def f_file_format_right_button():
    """文件格式确认"""
    try:
        with open('file_format.txt') as f:
            content = f.readlines()
        if (content[0] == 'all') or (content[0] == 'all\n'):
            add_settings('file_format', 'all')
            Log("保存文件格式为全部成功")
        else:
            new_content = []
            # 处理文件格式字符
            for i in content:
                if '\n' in i:
                    temp_name = list(i)
                    del temp_name[-1]
                    temp_name = ''.join(temp_name)
                    new_content.append(temp_name)
                elif '\n' not in i:
                    new_content.append(i)
            content = new_content[:]
            del new_content
            add_settings('file_format', content)
            Log("保存文件备份格式成功")
    except:
        pass

def f_cls_b():
    """清除日志内容"""
    with open('log/USBBackuper.log', 'w') as f:
        pass

def f_look_log_b():
    """查询日志"""
    def func():
        os.system('notepad.exe log/USBBackuper.log')
    look_th = threading.Thread(target=func, daemon=True)
    look_th.start()

def f_look_config_b():
    """查询配置"""
    def func():
        os.system('notepad.exe config/settings.json')
    look_th = threading.Thread(target=func, daemon=True)
    look_th.start()

def run_window():
    """运行设置录入窗口"""
    global root
    root.title('USBBackuper (By:Skyler Sun)')
    root.geometry('670x500+150+150')
    root.attributes('-alpha', 0.8)
    root.resizable(False, False)
    # 窗口组件
    # 单选框
    Rd_b1 = tk.Radiobutton(root, text="以U盘名称命名", command=Rd_button_1, variable=Rd_b1_status)
    Rd_b2 = tk.Radiobutton(root, text="以备份时间命名", command=Rd_button_2, variable=Rd_b2_status)
    Rd_b3 = tk.Radiobutton(root, text="以备份时间和U盘名称命名(recommended)", command=Rd_button_3, variable=Rd_b3_status)
    # u盘复制按钮
    disk_button = tk.Button(root, text="添加备份U盘", font=(20), command=f_disk_button)
    disk_right_button = tk.Button(root, text="确认", font=(20), command=f_disk_right_button)
    # 文件格式选择按钮
    file_format_button = tk.Button(root, text="添加备份文件格式", font=(20), command=f_file_format_button)
    file_format_right_button = tk.Button(root, text="确认", font=(20), command=f_file_format_right_button)
    # 退出按钮
    Exit_b = tk.Button(root, text="退出", bg='red', font=(30), width=670, command=Exit_button)
    # 剩余按钮
    run_b = tk.Button(root, text="开始备份", bg='green', font=(30), width=670, command=f_run_b)
    cls_b = tk.Button(root, text="清除日志", bg='blue', font=(30), width=670, command=f_cls_b)
    look_log_b = tk.Button(root, text="查看日志", font=(30), width=670, command=f_look_log_b)
    look_config_b = tk.Button(root, text="查看配置", font=(30), width=670, command=f_look_config_b)
    # 标签
    label1 = tk.Label(root, text="此处选择U盘文件备份后,文件夹的命名方式", fg='red', font=(20))
    label2 = tk.Label(root, text="选择要备份的U盘(按下按钮后在打开的文件里一行输入一个U盘卷标,只输入一行all表明全部)", fg='red', font=(20))
    label3 = tk.Label(root, text="选择备份文件格式(输入方式和上面相同,不带小数点,一行一个)", fg='red', font=(20))
    
    # 组件布局
    label1.place(x=0, y=0)
    label2.place(x=0, y=83)
    label3.place(x=0, y=150)

    Rd_b1.place(x=0, y=20)
    Rd_b2.place(x=0, y=40)
    Rd_b3.place(x=0, y=60)

    disk_button.place(x=5, y=110)
    disk_right_button.place(x=120, y=110)

    file_format_button.place(x=5, y=175)
    file_format_right_button.place(x=160, y=175)

    Exit_b.pack(side='bottom')
    cls_b.pack(side='bottom')
    look_log_b.pack(side='bottom')
    look_config_b.pack(side='bottom')
    run_b.pack(side='bottom')

    root.mainloop()
