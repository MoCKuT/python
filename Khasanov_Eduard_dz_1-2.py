def sum_list_calculation(sum_number):
    cal_list = 0
    indicator_1 = 0
    while indicator_1 <= 8:
        cal_number = sum_number % 10
        cal_list = cal_list + cal_number
        sum_number = sum_number // 10
        indicator_1 += 1
    return cal_list


my_list = []
n, n_b, n_c, i = 0, 0, 0, 0
answer = 0
answer_b = 0
answer_calculation = 0
number = 0
number_17 = 0

for i in range(1, 1000, 2):
    i = i ** 3
    my_list.append(i)

# Часть a ____________________________________________________
while n < len(my_list):
    number = my_list[n]
    calculation = sum_list_calculation(number) % 7
    if calculation == 0:
        answer_calculation = answer_calculation + number
    else:
        pass
    n += 1

print("Часть а", answer_calculation)

# Часть b ____________________________________________________
my_list_b = []
indicator = 0

while n_b < len(my_list):
    num = my_list[n_b] + 17
    my_list_b.append(num)
    n_b += 1

while indicator < len(my_list_b):
    number_b = my_list_b[indicator]
    calculation = sum_list_calculation(number_b) % 7
    if calculation == 0:
        answer_b = answer_b + number_b
    else:
        pass
    indicator += 1

print("Часть b", answer_b)

# Часть с ____________________________________________________
while n_c < len(my_list):
    number_17 = my_list[n_c]
    number_c = number_17 + 17
    calculation = sum_list_calculation(number_c) % 7
    if calculation == 0:
        answer = answer + number_c
    else:
        pass
    n_c += 1

print("Часть с", answer)
