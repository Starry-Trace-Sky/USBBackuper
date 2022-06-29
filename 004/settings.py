import json


file = 'config/settings.json'

def add_settings(key, value):
    """添加设置"""
    # 检查配置文件是否存在
    
    activate = False
    try:
        with open(file) as f:
            pass
    except:
        with open(file, 'w') as f:
            activate = True
            pass
    # 写入配置
    if activate:
        with open(file, 'a') as f:
            content_dict = {key:value}
            json.dump(content_dict, f, indent=4, ensure_ascii=False)
    elif not activate:
        with open(file) as f:
            file_content = json.load(f)
        # 读取内容后重新添加字典，再保存至文件
        file_content[key] = value
        with open(file, 'w') as f:
            json.dump(file_content, f, indent=4, ensure_ascii=False)

def read_settings():
    """读取配置"""
    with open(file) as f:
        result = json.load(f)
        return result
