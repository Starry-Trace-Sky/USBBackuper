import psutil, time, shutil, threading, os

from settings import read_settings
from log import get_time


def get_usb_name(volume):
    """通过cmd获取u盘卷名"""
    if ':' not in volume:
        volume += ':'
    if '/' in volume:
        volume = volume.split('/')[0]  # 处理后例如 G
    os.system('fsutil volume queryLabel ' + volume + ' > name.txt')
    path = 'name.txt'
    with open(path) as f:
        file_content = f.readlines()
    file_content = file_content[0].rstrip().split('是')[1]
    file_content = list(file_content)
    del file_content[0]
    del file_content[-1]
    usb_name = ''.join(file_content)
    return usb_name

def f_backup_th(path1):
        """复制线程"""
        with open('cache_file.txt', 'w') as f:
            pass
        disk_structure = os.walk(path1)
        for root, dirs, files in disk_structure:
            for i in files:
                with open('cache_file.txt', 'a') as f:
                    f.write(root + i + '\n')

def f_run_b():
    """开始运行"""
    # windows不会分配A,B盘符
    config_info = read_settings()
    """检测U盘"""
    older_usb_l = []
    while True:
        usb_name_list = []
        newer_usb_l = []
        disks = psutil.disk_partitions()
        # 获取当前USB设备列表
        for i in disks:
            if 'removable' in i.opts:
                newer_usb_l.append(i.mountpoint)
                usb_name_list.append(get_usb_name(i.mountpoint))
        older_usb_l = newer_usb_l[:]
        time.sleep(0.1)


if __name__ == '__main__':
    f_run_b()