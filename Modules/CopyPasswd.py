########################################################################
 # $ @Author: d1k3si
 # $ @Date: 2024-08-08 10:08:31
 # $ @LastEditors: d1k3si
 # $ @LastEditTime: 2024-08-08 20:22:04
 # $ @email:2098415680@qq.com
 # $ @Copyright (c) 2024 by d1k3si
########################################################################
from .LoadPasswd import load_yaml
import pyperclip
    
# 复制passwd到剪切板
def copy_passwd(pass_key:str):
    yaml_data=load_yaml()
    flag=False
    # 处理yaml_data==None
    try:
        for key in yaml_data.keys():
            if pass_key.lower()==key.lower():
                pyperclip.copy(yaml_data[pass_key])
                flag=True
    except Exception as e:
        print(f'error: {e}')

    if not flag:
        print('[-] 无效的pass_key,请使用show查看')
    else:
        print('[+] 密码已复制到剪切板')
            
