import psutil, time, shutil, threading, os

from settings import read_settings
from log import get_time


config_info = read_settings()

def get_usb_name(volume):
    """通过cmd获取u盘卷名"""
    # 只留下u盘对应字母
    if ':' not in volume:
        volume += ':'
    if '/' in volume:
        volume = volume.split('/')[0]
    os.system('fsutil volume queryLabel ' + volume + ' > name.txt')
    time.sleep(1)
    path = 'name.txt'
    with open(path) as f:
        file_content = f.readlines()
    file_content = file_content[0].rstrip().split('是')[1]
    file_content = list(file_content)
    del file_content[0]
    del file_content[-1]
    usb_name = ''.join(file_content)
    return usb_name


class f_backup_th:
    """复制线程"""
    def __init__(self, path1) -> None:
        self.path1 = path1
        self.path2 = path1.replace('\\', '/')
        self.file_l = []

    def init(self):
        self.disk_structure = os.walk(self.path1)
        self.name = get_usb_name(self.path1)

    def get_file(self) -> None:
        """将U盘文件导入内存"""
        self.file_l = []
        for root, dirs, files in self.disk_structure:
            if files != []:
                for i in files:
                    while '\\' in i:
                        i = i.replace('\\', '/')
                    self.file_l.append(root + '/' + i)

    def make_dir(self):
        """创建文件夹"""
        if config_info['f_name_format'] == 'both':
            now = get_time()
            while ':' in now:
                now = now.replace(':', '-')
            while '/' in now:
                now = now.replace('/', '-')
            try:
                os.mkdir(config_info['folder_position'] + '/' + now + self.name)
            except FileExistsError:
                pass
            return config_info['folder_position'] + '/' + now + self.name + '/'

    def run_f(self):
        """开始运行"""
        result = self.make_dir()
        if config_info['disk_choice'] == 'all':
            if config_info['file_format'] == 'all':
                shutil.copytree(self.path2, result)
            elif config_info['file_format'] != 'all':
                self.get_file()
                for i in self.file_l:
                    for ii in config_info['file_format']:
                        if ii in i:
                            shutil.copyfile(i, result + i.split('/')[-1])
        elif config_info['disk_choice'] != 'all':
            if self.name in config_info['disk_choice']:
                if config_info['file_format'] == 'all':
                    shutil.copytree(self.path2, result)
                elif config_info['file_format'] != 'all':
                    self.get_file()
                    for i in self.file_l:
                        for ii in config_info['file_format']:
                            if ii in i:
                                shutil.copyfile(i, result)

    def run(self):
        """开始运行"""
        self.init()
        threading.Thread(target=self.run_f, daemon=True).start()


def f_run_b():
    """开始运行"""
    # windows不会分配A,B盘符
    """检测U盘"""
    older_usb_l = []
    d_th = f_backup_th('D:\\')
    e_th = f_backup_th('E:\\')
    f_th = f_backup_th('F:\\')
    g_th = f_backup_th('G:\\')
    h_th = f_backup_th('H:\\')
    i_th = f_backup_th('I:\\')
    j_th = f_backup_th('J:\\')
    k_th = f_backup_th('K:\\')
    l_th = f_backup_th('L:\\')
    m_th = f_backup_th('M:\\')
    n_th = f_backup_th('N:\\')
    o_th = f_backup_th('O:\\')
    p_th = f_backup_th('P:\\')
    q_th = f_backup_th('Q:\\')
    r_th = f_backup_th('R:\\')
    s_th = f_backup_th('S:\\')
    t_th = f_backup_th('T:\\')
    u_th = f_backup_th('U:\\')
    v_th = f_backup_th('V:\\')
    w_th = f_backup_th('W:\\')
    x_th = f_backup_th('X:\\')
    y_th = f_backup_th('Y:\\')
    z_th = f_backup_th('Z:\\')
    th_directory = {'D:\\':d_th, 'E:\\':e_th, 'F:\\':f_th, 'G:\\':g_th, 'H:\\':h_th, 'I:\\':i_th, 
                    'J:\\':j_th, 'K:\\':k_th, 'L:\\':l_th, 'M:\\':m_th, 'N:\\':n_th, 'O:\\':o_th, 
                    'P:\\':p_th, 'Q:\\':q_th, 'R:\\':r_th, 'S:\\':s_th, 'T:\\':t_th, 'U:\\':u_th, 
                    'V:\\':v_th, 'W:\\':w_th, 'X:\\':x_th, 'Y:\\':y_th, 'Z:\\':z_th}
    while True:
        newer_usb_l = []
        disks = psutil.disk_partitions()
        # 获取当前USB设备列表
        for i in disks:
            if 'removable' in i.opts:
                newer_usb_l.append(i.mountpoint)
        for i in newer_usb_l:
            if i not in older_usb_l:
                # 新增的U盘处理
                th_directory[i].run()
        older_usb_l = newer_usb_l[:]
        time.sleep(0.1)


if __name__ == '__main__':
    f_run_b()