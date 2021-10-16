
price = [54.2, 48.6, 65.54, 13, 13.4, 11.6, 75.44, 21.32, 9.1, 12.2, 12.35]
i = 0
division_ruble, division_kopeck = '', ''
division_ruble_s, division_kopeck_s = '', ''
division_ruble_s_revers, division_kopeck_s_revers = '', ''
ruble, kopeck = ' руб ', ' коп '
n = 0

# Вывожу список цен и id списка
print(price)
print(id(price))
# Цикл для вывода цен в формате 00 руб 00 коп
while i < len(price):
    num = '%05.2f' % price[i]
    division_ruble = num[:2]
    division_kopeck = num[3:]
    print(division_ruble, ruble, division_kopeck, kopeck, end=" ")
    i += 1
print('')

# произвел сортировку списка по возрастанию
price.sort()

# Вывожу список цен и id списка (после сортировки)
print("")
print(price)
print(id(price))
# Цикл для вывода цен в формате 00 руб 00 коп (после сортировки)
while n < len(price):
    num = '%05.2f' % price[n]
    division_ruble_s = num[:2]
    division_kopeck_s = num[3:]
    print(division_ruble_s, ruble, division_kopeck_s, kopeck, end=" ")
    n += 1
print('')

# Сортировка по убыванию
price_sort = sorted(price, reverse=True)
print('')
# Вывод не обработанных цен
print(price_sort[0:5])
# Вывод цен в формате 00 руб 00 коп
n = 0
while n < 5:
    num = '%05.2f' % price_sort[n]
    division_ruble_s_revers = num[:2]
    division_kopeck_s_revers = num[3:]
    print(division_ruble_s_revers, ruble, division_kopeck_s_revers, kopeck, end=" ")
    n += 1
# Использовал print('') для отступа на экране вывода

