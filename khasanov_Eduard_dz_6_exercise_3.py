
users_dict = {}

if __name__ == '__main__':
    file_users = open('users.csv', 'r', encoding='utf-8')
    file_hobby = open('hobby.csv', 'r', encoding='utf-8')
    content_file_users = file_users.readlines()
    content_file_hobby = file_hobby.readlines()

    j = int(len(content_file_hobby) - 1)
    i = 0
    # Вывожу ошибку, если список хобби больше списка пользователи
    if len(content_file_hobby) > len(content_file_users):
        quit(1)
    else:
        for n in content_file_users:
            if i <= j:
                n = n.replace("\ufeff", "").replace('\n', '').replace(',', ' ').replace("'", '')
                users_dict[n] = content_file_hobby[i].replace("\ufeff", "").replace('\n', '').replace("'", "")
                i += 1
            else:
                users_dict[n] = None
    file_hobby.close()
    file_users.close()
    print(users_dict)

    with open('users_dict.txt', 'x', encoding='utf-8') as f:
        for key, val in users_dict.items():
            f.write('{} : {}\n'.format(key, val))
