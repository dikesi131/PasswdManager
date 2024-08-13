from .LoadPasswd import load_yaml
import re

# 检查是否有passwd重复
def find_duplicates() -> list:
    yaml_data=load_yaml()
    if not yaml_data:
        return None
    else:
        # dict.values() --> <class 'dict_values'>
        lst=list(yaml_data.values())
        return list(set([x for x in lst if lst.count(x) > 1]))

# 检查密码的安全性
def check_passwd_security(pass_key:str,passwd:str):
    patlower = '[a-z]+'
    patupper = '[A-Z]+'
    patdigit = '[0-9]+'
    patchara = '[!#$%&*-<=>?@^_|~]'
    d = {1:'弱密码', 2:'中低', 3:'中高', 4:'强密码'}
    r = [False] * 4
    if len(passwd) <= 6:
        r[0] = True
    else:
        for ch in passwd:
            if bool(re.search(patlower, ch)):
                r[0] = True
            elif bool(re.search(patupper, ch)):
                r[1] = True
            elif bool(re.search(patdigit, ch)):
                r[2] = True
            elif bool(re.search(patchara, ch)):
                r[3] = True

    if d.get(r.count(True))=='弱密码':
        print(f'[+] pass_key: {pass_key}对应密码为弱密码')