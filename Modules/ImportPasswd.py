from pathlib import Path
from .AddPasswd import add_special_passwd
import pandas as pd

# 导入txt文件中的pass_key和passwd
def import_from_txt(file_path:Path) -> dict:
    # 创建一个空字典来存储提取的 pass_key 和 passwd
    pass_dict = {}

    # 检查文件是否存在
    if not file_path.is_file():
        print(f"[-] 导入文件不存在")
        return None

    # 打开文件进行读取
    with file_path.open('r', encoding='utf-8') as file:
        while True:
            # 逐行读取文件
            line = file.readline()
            
            # 检查是否到达文件末尾
            if not line:
                break
            
            # 去掉行末的换行符和多余的空白字符
            line = line.strip()
            
            # 检查行是否包含冒号,忽略不以:分割的行
            if ':' in line:
                # 分割行，提取 pass_key 和 passwd
                pass_key, passwd = line.split(':', 1)
                
                # 去掉可能存在的前后空白字符
                pass_key = pass_key.strip()
                passwd = passwd.strip()
                
                # 将结果存入字典
                pass_dict[pass_key] = passwd

    return pass_dict

# 从csv导入pass_key和passwd
def import_from_csv(file_path:Path) -> dict:
    # 检查文件是否存在
    if not file_path.is_file():
        print(f"[-] 导入文件不存在")
        return None
    
    # use pandas
    # 使用自定义列
    name_list=['pass_key','passwd']
    # 提取前两列数据,忽略列名
    df = pd.read_csv(file_path,encoding="utf-8",header=0,names=name_list)
    
    # get pass_key
    pass_keys=df['pass_key'].tolist()
    # get passwd
    passwds=df['passwd'].tolist()
    # pass_dict={pass_key:passwd}
    pass_dict=dict(zip(pass_keys,passwds))

    return pass_dict

# 根据文件后缀选择对应的导入方法
def import_passwds(file_path:str):
    # 使用 pathlib.Path 创建路径对象
    path = Path(file_path)
    # 获取文件的后缀
    extension = path.suffix
    # 可导入的文件类型
    white_files=['.txt','.csv']
    if extension not in white_files:
        print(f'[-] 无效的文件类型,目前支持{white_files}')
    else:
        if extension.lower()=='.txt':
            pass_dict=import_from_txt(path)
            if len(pass_dict)==0:
                print('[-] 导入文件内容为空')
            else:
                for key,value in pass_dict.items():
                    add_special_passwd(key,value)
                print('[+] 导入成功,请使用show all查看')

        else:
            pass_dict=import_from_csv(path)
            if not pass_dict:
                print('[-] 导入文件内容为空')
            else:
                for key,value in pass_dict.items():
                    add_special_passwd(key,value)
                print('[+] 导入成功,请使用show all查看')


    
    
