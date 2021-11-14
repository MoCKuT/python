import os
import shutil

path_folder = r'H:\учеба\Khasanov_Eduard\khasanov_Eduard_dz_7\my_project'
destination = r'H:\учеба\Khasanov_Eduard\khasanov_Eduard_dz_7\my_project\templates'

if __name__ == '__main__':
    tree = os.walk(path_folder)
    if not os.path.exists(os.path.join(destination)):
        os.mkdir(os.path.join(destination))
        print("Папка создана")
        answer = str(1)
    else:
        print("Не удалось создать папку, папка уже существует")
        answer = str(input("1 - продолжить работу, 0 - выход: "))

    if answer == str(1):
        for n in tree:
            path_n = n[0].split("\\")
            if path_n[-1] == "templates" or path_n[-2] == "templates":
                continue
            if n[2]:
                try:
                    name = path_n[-1]
                    os.mkdir(os.path.join(destination, name))
                except FileExistsError as e:
                    print("(Ошибка) папка", path_n[-1], "существует. Имя изменено на", path_n[-2] + "_" + path_n[-1])
                    name = path_n[-2] + "_" + path_n[-1]
                    os.mkdir(os.path.join(destination, name))
                for file in n[2]:
                    start_path = os.path.join(n[0], file)
                    finish_path = os.path.join(destination, name, file)
                    shutil.copy2(start_path, finish_path)
    else:
        pass
