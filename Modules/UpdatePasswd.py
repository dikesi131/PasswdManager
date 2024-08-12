########################################################################
 # $ @Author: d1k3si
 # $ @Date: 2024-08-08 18:25:16
 # $ @LastEditors: d1k3si
 # $ @LastEditTime: 2024-08-12 00:08:17
 # $ @email:2098415680@qq.com
 # $ @Copyright (c) 2024 by d1k3si
########################################################################
from .LoadPasswd import load_yaml
from .AddPasswd import generate_alphaNum_password,generate_strong_password
from .GloVar import GetVar
import yaml

# 使用随机passwd更新 
def update_custom_passwd(pass_key:str,pass_mode:str):
    yaml_data=load_yaml()
    flag=False
    for key in yaml_data.keys():
        if pass_key.lower()==key.lower():
            if pass_mode.lower()=='normal':
                yaml_data[pass_key]=generate_alphaNum_password()
            else:
                yaml_data[pass_key]=generate_strong_password()

            flag=True

    if not flag:
        print('[-] 无效的pass_key,请使用show查看pass_key')
    else:
        with open(GetVar('passwd_path'), 'w', encoding='utf-8') as f:
            yaml.dump(data=yaml_data, stream=f, allow_unicode=True)

        print('[+] pass_key更新成功,请使用show [pass_key]查看')
        GetVar('g_logger').warning(f'[+] {pass_key}更新成功')
    

# 使用指定passwd更新
def update_special_passwd(pass_key:str,passwd:str):
    yaml_data=load_yaml()
    flag=False
    for key in yaml_data.keys():
        if pass_key.lower()==key.lower():
            yaml_data[pass_key]=passwd
            flag=True

    if not flag:
        print('[-] 无效的pass_key,请使用show查看pass_key')
    else:
        with open(GetVar('passwd_path'), 'w', encoding='utf-8') as f:
            yaml.dump(data=yaml_data, stream=f, allow_unicode=True)

        print('[+] pass_key更新成功,请使用show [pass_key]查看')
        GetVar('g_logger').warning(f'[+] {pass_key}更新成功')