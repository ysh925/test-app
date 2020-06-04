import yaml,os

def get_yaml(file_name):
    file_path = os.path.abspath('../') + os.sep + "Data" + os.sep + file_name + ".yaml"

    with open(file_path,'r',encoding='utf-8') as f:
        return yaml.load(f,Loader=yaml.FullLoader)


if __name__ == '__main__':
    a=get_yaml('ceshi')
    print(a)
