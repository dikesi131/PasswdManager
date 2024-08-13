########################################################################
 # $ @Author: d1k3si
 # $ @Date: 2024-08-08 18:25:15
 # $ @LastEditors: d1k3si
 # $ @LastEditTime: 2024-08-13 22:11:52
 # $ @email:2098415680@qq.com
 # $ @Copyright (c) 2024 by d1k3si
########################################################################
from .LoadPasswd import load_yaml
from .DestroyPasswd import clear_passwd
from .GloVar import GetVar
import yaml

def delete_passwd(pass_key:str):
    yaml_data=load_yaml()
    flag=False
    # 处理
    try:
        for key in yaml_data.keys():
            if pass_key.lower()==key.lower():
                flag=True
    except Exception as e:
        print(f'error: {e}')

    if not flag:
        print('[-] 无效pass_key,请使用show all查看pass_key')
    else:
        del yaml_data[pass_key]
        # 在yaml_data为空时,写入yaml会导致写入{}空字典,导致读取报错
        if yaml_data:
            with open(GetVar('passwd_path'), 'w', encoding='utf-8') as f:
                yaml.dump(data=yaml_data, stream=f, allow_unicode=True)
            print('[+] pass_key删除成功,请使用show all查看')
            GetVar('g_logger').warning(f'[+] {pass_key}删除成功')
        else:
            # 当yaml_data为空时,表明文件已清空,但不能用写入yaml_data的方式,而是直接清空文件
            clear_passwd()
