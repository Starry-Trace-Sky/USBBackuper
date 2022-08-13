from json import dump, load


file = 'config/settings.json'

def add_settings(key, value, utf_eight_code=0):
    """添加设置
    key和value均为字符串,对应键和值
    utf_eight_code为utf-8保存,默认未选择,选择传入1"""
    # 检查配置文件是否存在
    
    activate = False
    try:
        with open(file) as f:
            pass
    except:
        with open(file, 'w') as f:
            activate = True
            pass
    # 文件是否为空
    with open(file) as f:
        content = f.readlines()
    if content == []:
        activate = True
    # 写入配置
    if activate:
        with open(file, 'a') as f:
            content_dict = {key:value}
            if utf_eight_code == 0:
                dump(content_dict, f, indent=4, ensure_ascii=False)
            elif utf_eight_code == 1:
                dump(content_dict, f, indent=4, ensure_ascii=False, encoding='utf-8')
    elif not activate:
        with open(file) as f:
            file_content = json.load(f)
        # 读取内容后重新添加字典，再保存至文件
        file_content[key] = value
        with open(file, 'w') as f:
            dump(file_content, f, indent=4, ensure_ascii=False)

def read_settings():
    """读取配置"""
    with open(file) as f:
        result = load(f)
        return result
