from time import strftime


def get_time():
    time_now = strftime('%H') + ':' + strftime('%M') + ':' + strftime('%S')
    date_now = strftime('%Y') + '/' + strftime('%m') + '/' + strftime('%d')
    time_now = '[' + date_now + ' ' + time_now + ']'
    return time_now

def Log(write_content):
    """输出日志文件"""
    file = 'log/USBBackuper.log'
    time_now = get_time()
    # 检查日志文件是否存在
    try:
        with open(file) as f:
            pass
    except FileNotFoundError:
        with open(file, 'w') as f:
            pass
    # 写入日志内容
    with open(file, 'a', encoding='utf-8') as f:
        f.write(time_now + '\n')
        f.write(str(write_content) + '\n')
