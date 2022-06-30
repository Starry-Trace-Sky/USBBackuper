from settings import read_settings

import psutil, time


def f_run_b():
    """开始运行"""
    info = read_settings()
    def f_backup_th(path1, path2):
        """复制线程"""
        pass

    def f_check_th():
        """检测U盘"""
        older_usb_l = []
        while True:
            newer_usb_l = []
            disks = psutil.disk_partitions()
            for i in disks:
                if 'removable' in i.opts:
                    newer_usb_l.append(i.mountpoint)
            for i in newer_usb_l:
                if i not in older_usb_l:
                    print('copying')
            older_usb_l = newer_usb_l[:]
            time.sleep(0.1)

    f_check_th()


if __name__ == '__main__':
    f_run_b()