def nums_gen(number):
    for num in range(1, number + 1, 2):
        yield num


if __name__ == '__main__':
    max_number = int(input("введите верхний предел генератора: "))
    # Задание 1
    nums_order = nums_gen(max_number)
    for i in nums_order:
        print(i)
    print(type(nums_order))

    # Задание 2
    gen_num = (i for i in range(1, max_number + 1, 2))
    for i in gen_num:
        print(i)
    print(type(gen_num))
