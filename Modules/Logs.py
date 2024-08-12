########################################################################
 # $ @Author: d1k3si
 # $ @Date: 2024-08-11 22:49:52
 # $ @LastEditors: d1k3si
 # $ @LastEditTime: 2024-08-11 23:23:10
 # $ @email:2098415680@qq.com
 # $ @Copyright (c) 2024 by d1k3si
########################################################################
import logging
from .GloVar import _init,SetVar,GetVar
import time
_init()
# 日志初始化
def InitLogger():
    # 设置控制台日志处理程序
    # console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.DEBUG)

    # 设置文件日志处理程序,记录add/update/delete/rmall/sendpass/exit操作日志
    file_handler_access = logging.FileHandler('access.log',encoding='utf-8')
    file_handler_access.setLevel(logging.DEBUG)

    # 设置日志记录器
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(msecs)d %(name)s %(levelname)s \
                        %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')
    # 创建日志记录器
    SetVar('g_logger',logging.getLogger(__name__))
    # 日志内容不输出到控制台
    GetVar('g_logger').propagate = False

    GetVar('g_logger').setLevel(logging.DEBUG)
    # g_logger.addHandler(console_handler)
    GetVar('g_logger').addHandler(file_handler_access)

# 预处理
def PreTreatment():
    InitLogger()
    # 添加工具开头标志加入日志
    starting_banner = ('\n' + '-' * 70 + '\n' +
                   f"\n\tStarted At {time.ctime()}  @Athouer:dikesi\n"
                   + '\n\twelcome to use PasswdManager!'
                   + '\n\tIt can be used to manage your passwords'
                   + '\n\n' + '-' * 70 + '\n')
    GetVar('g_logger').info(f"{starting_banner}")
