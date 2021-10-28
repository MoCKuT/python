
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# Я сделал 4 варианта ответа, потому что не знаю какой из них будет действительно правильным
# Первый вариант (я понимаю, то что он подойдет только для не больших списков)
result = (el for el in src if src.count(el) == 1)
result_lst = []
for n in result:
    result_lst.append(n)
print("Вариант 1", result_lst)

# Второй вариант
order_src = []
remove_lst = []
for el in src:
    if el not in order_src:
        order_src.append(el)
    elif el not in remove_lst:
        remove_lst.append(el)

for el in remove_lst:
    order_src.remove(el)

print("Вариант 2", order_src)

# Третий вариант
lst = []
order_lst = (el and lst.append(el) if el not in lst else lst.remove(el) for el in src)
for n in order_lst:
    pass
print("Вариант 3", lst)

# Четвертый вариант (мне кажется этот вариант может подойти для больших списков)
order_lst_two = (el for el in src)
lst_two = []
remove_lst_two = []
for n in order_lst_two:
    if n not in lst_two:
        lst_two.append(n)
    elif n in lst_two:
        lst_two.remove(n)

for el in remove_lst_two:
    lst_two.remove(el)

print("Вариант 4", lst_two)
