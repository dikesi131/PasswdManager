from Modules import HelpInfo
from Modules import ShowPasswd
from Modules import AddPasswd
from Modules import UpdatePasswd
from Modules import DeletePasswd
from Modules import DestroyPasswd
from Modules import CheckPasswd
from Modules import SearchKey
from Modules import CopyPasswd
from Modules import EncryptPasswd
from Modules import SendPasswd
from Modules import ShowHistory
from Modules import ImportPasswd
from Modules import ExportPasswd
from Modules.GloVar import GetVar,SetVar
from Modules.LoadPasswd import load_yaml
from Modules import Logs
import re
import hashlib
import getpass
import os
import readline

# 清屏函数
def clear_screen():
    #\033[2J表示清除屏幕，\033[H表示将光标移动到第一行第一列
    print('\033[2J\033[H', end='')

# 自定义自动补全函数
def complete(text, state):
    commands=['help','info','show','add','update',
              'delete','rmall','exit','sendpass','searchpass',
              'copy','check','history','import','export']
    # all pass_key
    if not load_yaml():
        passkeys=[]
    else:
        passkeys=list(load_yaml().keys())

    # keywords in command
    keywords=['all','strong','normal','csv','txt']
    # 获取所有可能的自动补全选项
    options = [item for sublist in [commands, passkeys,keywords] for item in sublist]
    options = [option for option in options if option.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

# 需要用户输入主密钥才能使用脚本
def check_main_key() -> bool:
    # hash(main_key) --> a9b3d43042a0faefcb9e24844f443bb2b227fdc913677c48709f58889f2067a42b5e6b9415c0a6715835a3c517eac919c90ff7e73741b5f78c16f497494a1d50
    # getpass --> 无回显输入
    main_key = getpass.getpass("请输入主密钥: ")
    main_key_hash = hashlib.sha512(main_key.encode('utf-8')).hexdigest()
    if main_key_hash == 'a9b3d43042a0faefcb9e24844f443bb2b227fdc913677c48709f58889f2067a42b5e6b9415c0a6715835a3c517eac919c90ff7e73741b5f78c16f497494a1d50':
        # 解密passwd文件
        SetVar('se_key',hashlib.md5(main_key.encode('utf-8')).hexdigest())
        EncryptPasswd.Decryption(GetVar("en_passwd_path"),GetVar("passwd_path"),GetVar('se_key'))
        os.unlink(GetVar('en_passwd_path'))
        return True
    else:
        return False 

# 处理用户输入
def deal_input():
    # ANSI 转义码
    PURPLE = '\033[35m' # 紫色
    BOLD = '\033[1m' # 加粗
    RESET = '\033[0m' # 结尾标志
    text='PasswdManager> ' # text
    # 使用自动补全函数
    readline.set_completer(complete)
    readline.parse_and_bind('tab: complete')

    while(True):
        # 去除首部空格
        in_string=input(f'{PURPLE}{BOLD}{text}{RESET}').lstrip()
        if in_string.lower()=='help':
            HelpInfo.command_list()

        elif in_string.lower()=='info':
            HelpInfo.show_command_info('info')

        # 忽略大小写
        elif re.match('info',in_string,flags=re.I):
            # 匹配"info "之后的具体命令
            pattern = r'info\s+(.*)'
            match=re.search(pattern,in_string,flags=re.I)
            if match:
                HelpInfo.show_command_info(match.group(1))
            else:
                print('指令请用空格分隔,eg:info add')

        elif re.match('show',in_string,flags=re.I):
            # 匹配"show "之后的pass_key
            pattern = r'show\s+(.*)'
            match=re.search(pattern,in_string,flags=re.I)
            if match:
                ShowPasswd.show_passwd(match.group(1))
            else:
                print('指令请用空格分隔,eg:show [pass_key]')

        elif re.match('add',in_string,flags=re.I):
            pattern = r'add\s+(.*?)\s+(.*?)$'
            # 匹配"add "之后的pass_key和passwd or pass_mode
            match=re.search(pattern,in_string,flags=re.I)
            if match:
                pass_key=match.group(1)
                passwd_or_mode=match.group(2)
                if passwd_or_mode.lower() not in ['strong','normal']:
                    passwd=passwd_or_mode
                    AddPasswd.add_special_passwd(pass_key,passwd)
                else:
                    pass_mode=passwd_or_mode
                    AddPasswd.add_custom_passwd(pass_key,pass_mode)
            else:
                print('指令请用空格分隔,eg:add [pass_key] [passwd] or add [pass_key] [pass_mode]')

        elif re.match('update',in_string,flags=re.I):
            pattern = r'update\s+(.*?)\s+(.*?)$'
            # 匹配"update "后的pass_key和passwd or pass_mode
            match=re.search(pattern,in_string,flags=re.I)
            if match:
                pass_key=match.group(1)
                passwd_or_mode=match.group(2)
                if passwd_or_mode.lower() not in ['strong','normal']:
                    passwd=passwd_or_mode
                    UpdatePasswd.update_special_passwd(pass_key,passwd)
                else:
                    pass_mode=passwd_or_mode
                    UpdatePasswd.update_custom_passwd(pass_key,pass_mode)
            else:
                print('指令请用空格分隔,eg:update [pass_key] [passwd]')

        elif re.match('delete',in_string,flags=re.I):
            pattern=r'delete\s+(.*)'
            # 匹配"delete "后的pass_key
            match=re.search(pattern,in_string,flags=re.I)
            if match:
                DeletePasswd.delete_passwd(match.group(1))
            else:
                print('指令请用空格分隔,eg:delete [pass_key]')

        elif in_string=='':
            pass

        elif in_string.lower()=='rmall':
            ch=input('是否确定删除所有密码记录(y/n): ')
            if ch.lower()=='y':
                DestroyPasswd.clear_passwd()

        elif in_string.lower()=='check':
            if not CheckPasswd.find_duplicates():
                print('[-] 无重复密码')
            else:
                print(f'[+] 重复密码为:{CheckPasswd.find_duplicates()}')

        elif in_string.lower()=='searchpass':
            keys=SearchKey.get_keys_by_passwd()
            print(f'[+] 重复密码的pass_key为:{keys}')

        elif re.match('copy',in_string,flags=re.I):
            pattern=r'copy\s+(.*)'
            # 匹配"copy "后的pass_key
            match=re.search(pattern,in_string,flags=re.I)
            if match:
                CopyPasswd.copy_passwd(match.group(1))
            else:
                print('指令请用空格分隔,eg:copy [pass_key]')

        elif re.match('history',in_string,flags=re.I):
            pattern=r'history\s+(.*)'
            # 匹配"history "后的line_num
            match=re.search(pattern,in_string,flags=re.I)
            if match:
                ShowHistory.read_history(match.group(1))
            else:
                print('指令请用空格分隔,eg:history [line_num]')

        elif in_string.lower()=='sendpass':
            # send custom passwd
            SendPasswd.send_custom_passwd()
            # send storage passwd
            SendPasswd.send_storage_passwd()

        elif re.match('import',in_string,flags=re.I):
            pattern=r'import\s+(.*)'
            # 匹配"import "后的file_path
            match=re.search(pattern,in_string,flags=re.I)
            if match:
                ImportPasswd.import_passwds(match.group(1))
            else:
                print('指令请用空格分隔,eg:import [file_path]')

        elif re.match('export',in_string,flags=re.I):
            pattern=r'export\s+(.*)'
            # 匹配"export "后的file_type
            match=re.search(pattern,in_string,flags=re.I)
            if match:
                if match.group(1).lower()=='txt':
                    ExportPasswd.export_to_txt()
                elif match.group(1).lower()=='csv':
                    ExportPasswd.export_to_csv()
                else:
                    print('[-] 无效的导出格式,目前支持txt,csv')

        elif in_string.lower()=='exit':
            print('bye!')
            GetVar('g_logger').info('[+] PasswdManager exit!')
            return 0

        else:
            print('[-] 无效指令,请使用help查看可使用的命令')

def main():
    # 初始化全局变量及日志记录器
    Logs.PreTreatment()
    if check_main_key():
        try:
            deal_input()
        except Exception as e:
            print(f'error:{e}')
        finally:
            # encode and delete Passwd.yaml
            EncryptPasswd.Encryption(GetVar('passwd_path'),GetVar('en_passwd_path'),GetVar('se_key'))
            os.unlink(GetVar('passwd_path'))
    else:
        print('主密钥不正确,bye!')
        exit(0)
    
if __name__=='__main__':
    main()