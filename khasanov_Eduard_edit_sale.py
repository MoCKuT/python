import sys
#
#
# def position_line(num_line):
#
#

if __name__ == "__main__":
    edit_link, position, search = "", "", False
    # Проверка наличия аргументов
    if len(sys.argv) == 3:
        edit_link, new_link = sys.argv[1], sys.argv[2]
        edit_link = int(edit_link)
        with open("bakery.csv", "r+", encoding="utf-8") as f:
            content = " "
            i = 1
            # Использую цикл для поиска строки и позиции курсора
            while content:
                position = f.tell()
                line = f.readline()
                content = line.replace("\ufeff", "").replace('\n', '')
                if i == edit_link:
                    search = True
                    content = ""
                else:
                    pass
                i += 1
            # Если строка найдена то начинаю запись
            if search is True:
                f.seek(position)
                f.writelines(new_link)
                print("___Строка перезаписана___")
            else:
                print("В файле нет такой строки")
    else:
        print("Не указан номер строки или содержимое для ввода")
