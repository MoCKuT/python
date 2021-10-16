
lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

variable_boole, variable_str, variable_plus = True, '"', 0
element, enumerator = 0, 1
i, n = 0, 0

# Если я ничего не перепутал, то решение без создания нового списка
while i < len(lst):
    type_int, variable_plus = 0, 0
    element = lst[i]
    element_type = element
    # Если на нулевой позиции строки + или - то берем срез с первой позиции
    if (len(lst[i]) > 1) and (lst[i][0] == "+") or (lst[i][0] == "-"):
        element_type = lst[i][1:]
        variable_plus = 1
    else:
        pass
    # Проверяю строку на число
    element_type = element_type.isdigit()
    # Если это число то меняем его формат
    if element_type == variable_boole:
        # Возвращаю + к числам у которых они были
        if variable_plus == 1:
            lst[i] = "+" + "{:02}".format(int(lst[i]))
        else:
            lst[i] = "{:02}".format(int(lst[i]))
        lst.insert(i, variable_str)
        i += 2
        lst.insert(i, variable_str)
    else:
        pass
    i += 1

# формирую вывод списка
while n < len(lst):
    if lst[n] == variable_str:
        enumerator += 1
        if (enumerator % 2) == 0:
            print(lst[n], end='')
        else:
            print(lst[n], end=' ')
    else:
        if (enumerator % 2) == 0:
            print(lst[n], end='')
        else:
            print(lst[n], end=' ')
    n += 1
