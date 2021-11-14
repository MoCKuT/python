import os


project = {
    "my_project": {
        "settings": {},
        "mainapp": {},
        "adminapp": {},
        "autapp": {}
    }
}

if __name__ == '__main__':
    for key, val in project.items():
        if type(val) == dict:
            if os.path.exists(key):
                print("Папка существует")
                break
            os.mkdir(key)
            for key_2, val_2 in val.items():
                if type(val_2) == dict:
                    dir_path = os.path.join(key, key_2)
                    os.mkdir(dir_path)
    else:
        print("Шаблон создан")
