def digital_list_remain(digit_remain):
    i = 1
    while i < 3:
        digit_crushing = digit_remain % 10
        digit_list.insert(0, digit_crushing)
        digit_remain = digit // 10
        i += 1


percent_one = " процент"
percent_two = " процента"
percent_three = " процентов"
word = ""
n = 0,
digit_crushing = 0
digit = int(1)
digit_remain = 0

while digit <= 100:
    digit_list = []
    digital_list_remain(digit)
    if (digit_list[1] == 1) and (digit_list[0] != 1):
        word = percent_one
    elif (digit_list[1] > 1) and (digit_list[1] < 5) and (digit_list[0] != 1):
        word = percent_two
    else:
        word = percent_three
    del digit_list
    print(str(digit) + word)
    digit += 1

