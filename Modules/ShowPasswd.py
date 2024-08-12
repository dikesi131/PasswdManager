########################################################################
 # $ @Author: d1k3si
 # $ @Date: 2024-08-07 19:32:42
 # $ @LastEditors: d1k3si
 # $ @LastEditTime: 2024-08-08 20:22:46
 # $ @email:2098415680@qq.com
 # $ @Copyright (c) 2024 by d1k3si
########################################################################
from .LoadPasswd import load_yaml
    
def show_passwd(pass_key:str):
    yaml_data=load_yaml()
    flag=False
    if not yaml_data:
        print('[+] 无密码记录,可使用add命令添加记录')
    else:
        if pass_key.lower()=='all':
            num=1
            print('|pass_key|'.ljust(30,' ') + '|passwd|'.ljust(20,' '))
            print('-'*50)
            for key,value in yaml_data.items():
                print(f'[{num}]{key}'.ljust(30,' ') + f'{value}'.ljust(20,' '))
                num+=1
        else:
            for key in yaml_data.keys():
                if pass_key.lower()==key.lower():
                    print('|pass_key|'.ljust(30,' ') + '|passwd|'.ljust(20,' '))
                    print(f'{key}'.ljust(30,' ') + f'{yaml_data[key]}'.ljust(20,' '))
                    flag=True
            
            if not flag:
                print('[-] 无效的pass_key')
    
