from .LoadPasswd import load_yaml

# 检查是否有passwd重复
def find_duplicates() -> list:
    yaml_data=load_yaml()
    # dict.values() --> <class 'dict_values'>
    lst=list(yaml_data.values())
    return list(set([x for x in lst if lst.count(x) > 1]))