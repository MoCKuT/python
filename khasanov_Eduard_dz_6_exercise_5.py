
if __name__ == '__main__':

    file_read_1 = input("Имя файла с пользователями: ")
    file_read_2 = input("Имя файла с хобби: ")
    file_write = input("Имя файла для записи: ")

    f_hobby = open(file_read_2, 'r', encoding='utf-8')

    with open(file_read_1, 'r', encoding='utf-8') as f_user:
        for line in f_user:
            content_line = line.replace("\ufeff", "").replace('\n', '').replace(",", " ")
            content = f_hobby.readline()
            content_clean = content.replace("\ufeff", "").replace('\n', '')
            if content_clean == '':
                content_clean = None
            else:
                pass
            with open(file_write, 'a', encoding='utf-8') as f:
                f.write('{}: {}\n'.format(content_line, content_clean))
    error = f_hobby.readline()
    if error != '':
        print("Ошибка длинны файлов")
        quit(1)
    else:
        pass
    f_hobby.close()
    print("_" * 8 + "Файл записан" + "_" * 8)
