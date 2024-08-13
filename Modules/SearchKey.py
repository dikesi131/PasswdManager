from .CheckPasswd import find_duplicates
from .LoadPasswd import load_yaml

# 根据passwd-->pass_key
def get_keys_by_passwd() -> list:
    keys = []
    yaml_data=load_yaml()
    values=find_duplicates()
    if not values:
        return None
    else:
        for key, val in yaml_data.items():
            if val in values:
                keys.append(key)
        return keys