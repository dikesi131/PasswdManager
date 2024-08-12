########################################################################
 # $ @Author: d1k3si
 # $ @Date: 2024-08-11 00:30:45
 # $ @LastEditors: d1k3si
 # $ @LastEditTime: 2024-08-11 22:52:41
 # $ @email:2098415680@qq.com
 # $ @Copyright (c) 2024 by d1k3si
########################################################################

# 初始化全局变量
def _init():
    """在主模块初始化"""
    global GLOBALS_DICT
    # 设置全局变量默认值
    GLOBALS_DICT = {
        # 日志变量
        'g_logger':None,
        # passwd存储文件路径
        'passwd_path':'Passwd/Passwd.yaml',
        # 加密passwd文件存储路径
        'en_passwd_path':'Passwd/en_Passwd.aes',
        # 次级密钥，由主密钥产生
        'se_key':'',
        # 导出文件目录
        'export_dic':'passwd_export',
        # 导出的txt文件
        'export_txt':'export.txt',
        # 导出的csv文件
        'export_csv':'export.csv'
    }
 
# 用于设置全局变量
def SetVar(name:str, value) -> bool:
    """设置Config"""
    try:
        GLOBALS_DICT[name] = value
        return True
    except KeyError:
        return False
 
# 用于获取全局变量
def GetVar(name:str):
    """取值Config"""
    try:
        return GLOBALS_DICT[name]
    except KeyError:
        return "Not Found"
