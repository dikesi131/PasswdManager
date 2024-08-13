########################################################################
 # $ @Author: d1k3si
 # $ @Date: 2024-08-07 17:32:59
 # $ @LastEditors: d1k3si
 # $ @LastEditTime: 2024-08-13 21:40:04
 # $ @email:2098415680@qq.com
 # $ @Copyright (c) 2024 by d1k3si
########################################################################
def command_list():
    print('可使用的命令如下 (使用tab键能补全命令):')
    print('help\t\tinfo\t\tshow\t\tadd\t\tupdate')
    print('delete\t\tcopy\t\tcheck\t\tsearchpass\tsendpass')
    print('history\t\timport\t\texport\t\trmall\t\texit')

def show_command_info(cmd_name:str):
    # 忽略大小写
    if cmd_name.lower()=='help':
        print('help'.ljust(16,' ') + ':显示可使用的所有命令')

    elif cmd_name.lower()=='info':
        print('info'.ljust(16,' ') + ':显示命令的具体使用方法')
        print('usage'.ljust(16,' ') + '- info [command_name]')
        print('eg'.ljust(16,' ')+ '- info add')

    elif cmd_name.lower()=='show':
        print('show'.ljust(16,' ') + ':显示相应密码')
        print('usage'.ljust(16,' ') + '- show [pass_key] (使用tab键能补全pass_key)')
        print('usage'.ljust(16,' ') + '- show all (all表示显示所有pass_key和passwd)')
        print('eg'.ljust(16,' ') + '- show bilibili')

    elif cmd_name.lower()=='add':
        print('add'.ljust(16,' ') + ':添加密码记录 (使用tab键能补全pass_key)')
        print('usage'.ljust(16,' ') + '- add [pass_key] [passwd] (请不要使用strong和normal作为passwd,不区分大小写)')
        print('eg'.ljust(16,' ') + '- add bilibili 123456')
        print('usage'.ljust(16,' ') + '- add [pass_key] [pass_mode] (使用随机生成的密码)')
        print('eg'.ljust(16,' ') + '- add bilibili strong/normal (strong表示数字+大小写字母+特殊字符,normal没有特殊字符)')
        
    elif cmd_name.lower()=='update':
        print('update'.ljust(16,' ') + ':更新密码记录 (使用tab键能补全pass_key)')
        print('usage'.ljust(16,' ') + '- update [pass_key] [passwd] (请不要使用strong和normal作为passwd,不区分大小写)')
        print('eg'.ljust(16,' ') + '- update bilibili 123456')
        print('usage'.ljust(16,' ') + '- update [pass_key] [pass_mode] (使用随机生成的密码)')
        print('eg'.ljust(16,' ') + '- update bilibili strong/normal (strong表示数字+大小写字母+特殊字符,normal没有特殊字符)')

    elif cmd_name.lower()=='delete':
        print('delete'.ljust(16,' ') + ':删除密码记录 (使用tab键能补全pass_key)')
        print('usage'.ljust(16,' ') + '- delete [pass_key]')
        print('eg'.ljust(16,' ') + '- delete bilibili')

    elif cmd_name.lower()=='copy':
        print('copy'.ljust(16,' ') + ':复制密码到剪切板 (使用tab键能补全pass_key)')
        print('usage'.ljust(16,' ') + '- copy [pass_key]')
        print('eg'.ljust(16,' ') + '- copy bilibili')

    elif cmd_name.lower()=='check':
        print('check'.ljust(16,' ') + ':检查是否有密码重复并且列出弱密码')

    elif cmd_name.lower()=='searchpass':
        print('searchpass'.ljust(16,' ') + ':查找密码重复的pass_key,该指令可配合check使用')

    elif cmd_name.lower()=='sendpass':
        print('sendpass'.ljust(16,' ') + ':发送生成的随机密码和存储的密码给指定邮箱 (配置文件为Config.yaml)')

    elif cmd_name.lower()=='history':
        print('history'.ljust(16,' ') + ':显示操作记录')
        print('usage'.ljust(16,' ') + '- history [line_num]')
        print('eg'.ljust(16,' ') + '- history 20')

    elif cmd_name.lower()=='import':
        print('import'.ljust(16,' ') + ':导入特定格式的密码文件')
        print('usage'.ljust(16,' ') + '- import [file_path] (txt,csv)')
        print('eg'.ljust(16,' ') + '- import test.csv')

    elif cmd_name.lower()=='export':
        print('export'.ljust(16,' ') + ':导出为特定格式的密码文件')
        print('usage'.ljust(16,' ') + '- export [file_type] (txt,csv)')
        print('eg'.ljust(16,' ') + '- export csv')

    elif cmd_name.lower()=='rmall':
        print('rmall'.ljust(16,' ') + ':删除所有密码记录 (高危操作,请慎重)')

    elif cmd_name.lower()=='exit':
        print('exit'.ljust(16,' ') + ':退出PasswdManager')

    else:
        print('无效命令,请使用help查看可使用的命令')
