########################################################################
 # $ @Author: d1k3si
 # $ @Date: 2024-08-08 18:25:15
 # $ @LastEditors: d1k3si
 # $ @LastEditTime: 2024-08-12 00:05:27
 # $ @email:2098415680@qq.com
 # $ @Copyright (c) 2024 by d1k3si
########################################################################
from .LoadPasswd import load_yaml
from .GloVar import GetVar
import string
import secrets
import yaml

# 生成16位数字+大小写字母密码
def generate_alphaNum_password(length=16) -> string:
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# 生成16位数字+大小写+特殊字符的强密码
def generate_strong_password(length=16) -> string:
    normal_special='!#$%&*-<=>?@^_|~'
    alphabet = string.ascii_letters + string.digits + normal_special
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# 检查添加时pass_key是否重复
def check_passkey(pass_key:str) -> bool:
    yaml_data=load_yaml()
    # 当yaml_data为None时表明此时yaml文件为空,直接返回False
    if not yaml_data:
        return False
    
    return pass_key in yaml_data.keys()

# 添加随机密码
def add_custom_passwd(pass_key:str,pass_mode:str):
    if check_passkey(pass_key):
        print('[-] pass_key已存在,请使用show [pass_key]查看')
    else:
        add_dict=dict()
        # 写入随机密码
        # 数字+大小写字母
        if pass_mode.lower()=='normal':
            costom_passwd=generate_alphaNum_password()
            # 添加到字典
            add_dict.setdefault(pass_key,costom_passwd)
        else:
            costom_passwd=generate_strong_password()
            add_dict.setdefault(pass_key,costom_passwd)
        
        with open(GetVar('passwd_path'), 'a', encoding='utf-8') as f:
            yaml.dump(data=add_dict, stream=f, allow_unicode=True)

        print('[+] pass_key添加成功,请使用show [pass_key]查看')
        GetVar('g_logger').warning(f'[+] {pass_key}添加成功')

# 添加指定密码
def add_special_passwd(pass_key:str,passwd:str):
    if check_passkey(pass_key):
        print('[-] pass_key已存在,请使用show [pass_key]查看')
    else:
        add_dict=dict()
        add_dict.setdefault(pass_key,passwd)

        with open(GetVar('passwd_path'), 'a', encoding='utf-8') as f:
            yaml.dump(data=add_dict, stream=f, allow_unicode=True)
            
        print('[+] pass_key添加成功,请使用show [pass_key]查看')
        GetVar('g_logger').warning(f'[+] {pass_key}添加成功')

