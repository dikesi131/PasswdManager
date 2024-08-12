# PasswdManager

由于开发者自已发现使用的密码存在多个重复，考虑到安全性问题，遂开发了一款基于python的本地化、命令行交互的密码管理器。

实际上，如果考虑到设备更换等问题，建议定期将密码文件备份（云备份/本地备份等等）

## 使用方法

```cmd
 pip install -r requirements.txt
 python3 PasswdExec.py
```

>使用后进入交互式界面，可使用help查看所有命令，info查看命令具体使用方法

```cmd
可使用的命令如下 (使用tab键能补全命令):
help            info            show            add             update
delete          copy            check           searchpass      sendpass
history         import          export          rmall           exit
```

## 项目实现功能

考虑到密码的复杂性，项目支持用户自已设置密码或者使用系统生成的随机密码，随机密码默认为16位，有以下两种类型

>normal：大小写字母+数字（满足大多数安全性要求）
>
>strong：大小写字母+数字+部分特殊字符（满足更严苛的安全性要求）

- 增添密码记录

```cmd
add             :添加密码记录 (使用tab键能补全pass_key)
usage           - add [pass_key] [passwd] (请不要使用strong和normal作为passwd,不区分大小写)
eg              - add bilibili 123456
usage           - add [pass_key] [pass_mode] (使用随机生成的密码)
eg              - add bilibili strong/normal (strong表示数字+大小写字母+特殊字符,normal没有特殊字符)
```

- 删除密码记录

```cmd
delete          :删除密码记录 (使用tab键能补全pass_key)
usage           - delete [pass_key]
eg              - delete bilibili
```

- 修改密码

```cmd
update          :更新密码记录 (使用tab键能补全pass_key)
usage           - update [pass_key] [passwd] (请不要使用strong和normal作为passwd,不区分大小写)
eg              - update bilibili 123456
usage           - update [pass_key] [pass_mode] (使用随机生成的密码)
eg              - update bilibili strong/normal (strong表示数字+大小写字母+特殊字符,normal没有特殊字符)
```

- 查看密码记录

```cmd
show            :显示相应密码
usage           - show [pass_key] (使用tab键能补全pass_key)
usage           - show all (all表示显示所有pass_key和passwd)
eg              - show bilibili
```

- 检查密码安全性

```cmd
check           :检查是否有密码重复
```

- 查找密码相同的记录

```cmd
searchpass      :查找密码重复的pass_key,该指令可配合check使用
```

- 销毁所有密码记录

```cmd
rmall           :删除所有密码记录 (高危操作,请慎重)
```

- 从特定格式文件导入密码记录

```cmd
import          :导入特定格式的密码文件
usage           - import [file_path] (txt,csv)
eg              - import test.csv
```

- 导出密码记录

```cmd
export          :导出为特定格式的密码文件
usage           - export [file_type] (txt,csv)
eg              - export csv
```

- 发送密码记录

```cmd
sendpass        :发送生成的随机密码和存储的密码给指定邮箱 (配置文件为Config.yaml)
```

## 如何更改主密钥？

>考虑到项目的安全性，在使用脚本前需要输入主密钥，当主密钥正确时，密码文件才会解密并且可以进行密钥管理。
>
>使用前请重新设置主密钥

- PasswdExec.py/`check_main_key()`

```py
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
```

>该函数进行主密钥的校验，判断主密钥的sha512值是否匹配，所以如果需要更换主密钥，只需要将hash值改为更换的主密钥的sha512值即可
>
>如123456 --> sha512() --> ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413

## 如何导入密码记录？

>目前仅支持txt和csv两种格式文件进行导入

txt文件格式要求如下：

- pass_key和passwd以`:`分隔

```sh
# example.txt

admin:admin
test:test
```

csv文件格式要求如下：

- 第一列为pass_key,第二列为passwd
- 分隔符为`,`

```sh
# 列名可以不为pass_key和passwd
column1,column2
admin,admin
test,test
```

## 如何使用发送密钥功能？

>发送密钥功能配置文件为`Config.yaml`，功能采用邮箱发送实现，以下以QQ邮箱为例（邮箱需要开启SMTP功能）

```yaml
# Config.yaml

# 发件人
email: xxxxx@qq.com
# 邮箱授权码
PassCode: xxxxx
# SMTP服务端口(默认为25)
port: 25
# 收件人
SendTo: xxxx@qq.com
```

