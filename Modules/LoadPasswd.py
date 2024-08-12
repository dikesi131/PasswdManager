from .GloVar import GetVar
import yaml

# load Passwd.yaml
def load_yaml() -> dict:
    with open(GetVar('passwd_path'), 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
        return result