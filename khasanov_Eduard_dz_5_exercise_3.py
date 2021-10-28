
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if __name__ == '__main__':
    # Генератор
    j = int(len(classes) - 1)
    couples_gen = (((tutors[i], classes[i]) if (i <= j) else (tutors[i], None)) for i in range(0, len(tutors)))

    # Вывод генератора
    for n in couples_gen:
        print(n, type(n))
    print(type(couples_gen))

