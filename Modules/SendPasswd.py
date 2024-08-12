########################################################################
 # $ @Author: d1k3si
 # $ @Date: 2024-08-08 19:59:27
 # $ @LastEditors: d1k3si
 # $ @LastEditTime: 2024-08-12 00:07:38
 # $ @email:2098415680@qq.com
 # $ @Copyright (c) 2024 by d1k3si
########################################################################
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from .AddPasswd import generate_alphaNum_password,generate_strong_password
from .LoadPasswd import load_yaml
from .GloVar import GetVar
import smtplib
import yaml

# load config
def load_config():
    with open('Config.yaml', 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
        return result

# 发送生成的随机密码
def send_custom_passwd(passwd_count=5):
    yaml_data=load_config()
    # code为QQ邮箱开启SMTP服务后的授权码
    SenderConfig={'email': yaml_data['email'],'code':yaml_data['PassCode']}
    # from-->发件人
    # to-->收件人
    # subject:主题
    EmailContent={'from':yaml_data['email'],'to':yaml_data['SendTo'],
                 'subject':'Send Custom Passwd to Phone'}
    # 电子邮件内容设置
    msg = MIMEMultipart()
    msg['From'] = EmailContent['from']
    msg['To'] = Header(EmailContent['to'],'utf-8')
    msg['Subject'] = Header(EmailContent['subject'],'utf-8')

    text_lines=[]

    text_lines.append('[normal level passwd]')
    # create normal level passwd
    for i in range(passwd_count):
        text_line=f'[{i}]:{generate_alphaNum_password()}'
        text_lines.append(text_line)

    # 分割线
    text_lines.append('-'*30)

    # create strong level passwd
    text_lines.append('[strong level passwd]')
    for j in range(passwd_count):
        test_line=f'[{j}]:{generate_strong_password()}'
        text_lines.append(test_line)

    # list --> string with \n
    message='\n'.join(text_lines)
    
    # 添加正文
    msg.attach(MIMEText(message, 'plain'))
    
    # 创建 SMTP 客户端
    try:
        # 链接邮箱服务器，SMTP默认端口为25
        with smtplib.SMTP('smtp.qq.com', yaml_data['port']) as smtp:
            smtp.starttls()
            smtp.login(SenderConfig['email'], SenderConfig['code'])
            smtp.send_message(msg)
        print('[+] 邮件发送成功')
        GetVar('g_logger').warning(f"[+] 邮件发送成功,send custom passwd to {yaml_data['SendTo']}")
    except Exception as e:
        print(f"[-] 邮件发送失败: {e}")

# 发送存储的密码
def send_storage_passwd():
    yaml_data=load_config()
    # code为QQ邮箱开启SMTP服务后的授权码
    SenderConfig={'email': yaml_data['email'],'code':yaml_data['PassCode']}
    # from-->发件人
    # to-->收件人
    # subject:主题
    EmailContent={'from':yaml_data['email'],'to':yaml_data['SendTo'],
                 'subject':'Send Storage Passwd to Phone'}
    # 电子邮件内容设置
    msg = MIMEMultipart()
    msg['From'] = EmailContent['from']
    msg['To'] = Header(EmailContent['to'],'utf-8')
    msg['Subject'] = Header(EmailContent['subject'],'utf-8')

    text_lines=[]
    pass_data=load_yaml()
    index=0
    for key,value in pass_data.items():
        text_line=f'[{index}]{key}:\t{value}'
        text_lines.append(text_line)
        index+=1

    # list --> string with \n
    message='\n'.join(text_lines)
    
    # 添加正文
    msg.attach(MIMEText(message, 'plain'))
    
    # 创建 SMTP 客户端
    try:
        # 链接邮箱服务器，SMTP默认端口为25
        with smtplib.SMTP('smtp.qq.com', yaml_data['port']) as smtp:
            smtp.starttls()
            smtp.login(SenderConfig['email'], SenderConfig['code'])
            smtp.send_message(msg)
        print('[+] 邮件发送成功')
        GetVar('g_logger').warning(f"[+] 邮件发送成功,send storage passwd to {yaml_data['SendTo']}")
    except Exception as e:
        print(f"[-] 邮件发送失败: {e}")