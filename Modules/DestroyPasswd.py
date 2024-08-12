########################################################################
 # $ @Author: d1k3si
 # $ @Date: 2024-08-07 23:45:26
 # $ @LastEditors: d1k3si
 # $ @LastEditTime: 2024-08-11 23:25:11
 # $ @email:2098415680@qq.com
 # $ @Copyright (c) 2024 by d1k3si
########################################################################
from .GloVar import GetVar
# 清空
def clear_passwd():
    with open(GetVar('passwd_path'), encoding="utf-8", mode="w") as f:
        f.truncate()

    print('[+] 所有密码记录已清除')
    GetVar('g_logger').warning('[+] 所有密码记录已清除')