from pathlib import Path
from .GloVar import GetVar
from .LoadPasswd import load_yaml
import pandas as pd

# 检查导出目录是否存在,不存在则新建
def check_export_directory():
    # 获取当前目录
    current_directory = Path.cwd() / 'PasswdManager'
    
    # 定义目标目录路径
    target_directory = current_directory / GetVar('export_dic')
    
    # 检查目录是否存在
    if not target_directory.exists():
        # 如果目录不存在，则创建目录
        target_directory.mkdir(parents=True, exist_ok=True)

# 导出为txt文件
def export_to_txt():
    check_export_directory()
    yaml_data=load_yaml()
    export_path=GetVar('export_dic') + '/' + GetVar('export_txt')
    try:
        with open(export_path,'w',encoding='utf-8') as f:
            for key,value in yaml_data.items():
                f.write(f'{key}:{value}\n')

        print(f'[+] 导出txt成功,文件路径:{export_path}')
    except Exception as e:
        print(f'error: {e}')

# 导出为csv文件
def export_to_csv():
    check_export_directory()
    yaml_data=load_yaml()
    export_path=GetVar('export_dic') + '/' + GetVar('export_csv')
    pass_keys=yaml_data.keys()
    passwds=yaml_data.values()
    # pass_key,passwd 是列名
    csv_data=pd.DataFrame({'pass_key':pass_keys,'passwd':passwds})
    try:
        # 使用utf-8还是会中文乱码,需要使用utf_8_sig
        csv_data.to_csv(export_path,index=False,sep=',',encoding='utf_8_sig')
        print(f'[+] 导出csv成功,文件路径:{export_path}')
    except Exception as e:
        print(f'error: {e}')
