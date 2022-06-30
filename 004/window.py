import tkinter as tk
from log import Log
from settings import add_settings, read_settings


root = tk.Tk()
file_name_format = None
Rd_b1_status = tk.IntVar()
Rd_b2_status = tk.IntVar()
Rd_b3_status = tk.IntVar()
Rd_b1_status.set(0)
Rd_b2_status.set(0)
Rd_b3_status.set(0)

def Rd_button_1():
    """文件拷贝选择1"""
    global file_name_format, Rd_b1_status
    file_name_format = 'disk'
    Log("U盘拷贝命名格式设置为U盘名称")
    Log("保存至配置文件中...")
    add_settings('f_name_format', file_name_format)
    Log("保存成功")
    Rd_b2_status.set(0)
    Rd_b3_status.set(0)

def Rd_button_2():
    """文件拷贝选择2"""
    global file_name_format, Rd_b2_status
    file_name_format = 'time'
    Log("U盘拷贝命名格式设置为时间")
    Log("保存至配置文件中...")
    add_settings('f_name_format', file_name_format)
    Log("保存成功")
    Rd_b1_status.set(0)
    Rd_b3_status.set(0)

def Rd_button_3():
    """文件拷贝选择3"""
    global file_name_format, Rd_b3_status
    file_name_format = 'both'
    Log("U盘拷贝命名格式设置为两者")
    Log("保存至配置文件中...")
    add_settings('f_name_format', file_name_format)
    Log("保存成功")
    Rd_b1_status.set(0)
    Rd_b2_status.set(0)

def run_window():
    """运行设置录入窗口"""
    global root
    root.title('USBBackuper (By:Skyler Sun)')
    root.geometry('450x500+150+150')
    root.attributes('-alpha', 0.8)
    root.attributes('-topmost', True)
    # 窗口组件
    # 单选框
    Rd_b1 = tk.Radiobutton(root, text="以U盘名称命名", command=Rd_button_1, variable=Rd_b1_status)
    Rd_b2 = tk.Radiobutton(root, text="以拷贝时间命名", command=Rd_button_2, variable=Rd_b2_status)
    Rd_b3 = tk.Radiobutton(root, text="以拷贝时间和U盘名称命名(recommended)", command=Rd_button_3, variable=Rd_b3_status)
    # 退出按钮
    Exit_b = tk.Button(root, text="退出", bg='red', font=(30), width=10)
    # 标签
    label1 = tk.Label(root, text="此处选择U盘文件拷贝后,文件夹的命名方式", fg='red', font=(20))
    
    # 组件布局
    label1.place(x=0, y=0)
    Rd_b1.place(x=0, y=20)
    Rd_b2.place(x=0, y=40)
    Rd_b3.place(x=0, y=60)
    Exit_b.place(x=340, y=460)

    root.mainloop()
