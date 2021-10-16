
my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
i, n, = 0, 0
hello = "Привет, "
hey_name = ""
space = " "
symbol_name = ""

# решение без создания списка
while n < len(my_list):
    i = -1
    welcome_name = ""
    name_b = my_list[n]
    while i < len(name_b):
        symbol_name = name_b[i]
        if symbol_name != space:
            welcome_name = symbol_name + welcome_name
            i -= 1
        else:
            i = len(name_b)
    n += 1
    print(hello + welcome_name.title())
