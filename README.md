# PasswdManager

由于开发者自已发现使用的密码存在多个重复，考虑到安全性问题，遂开发了一款基于python的本地化、命令行交互的密码管理器。

实际上，如果考虑到设备更换等问题，建议定期将密码文件备份（云备份/本地备份等等）

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

