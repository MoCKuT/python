import os
from time import perf_counter


def size_item(arg_1, arg_2):
    return os.stat(os.path.join(arg_1, arg_2)).st_size


folder = r'some_data'
start = perf_counter()
size_100 = 100
size_1000 = 1000
size_10000 = 10000
size_100000 = 100000
lst_100, lst_1000, lst_10000, lst_100000, lst_more = [], [], [], [], []

if __name__ == '__main__':
    files_sort = (item
                  for item in os.listdir(folder)
                  )
    for n in files_sort:
        file = n
        size = size_item(folder, n)
        if size < size_100:
            lst_100.append(n)
        elif (size < size_1000) and (size > size_100):
            lst_1000.append(n)
        elif (size < size_10000) and (size > size_1000):
            lst_10000.append(n)
        elif (size < size_100000) and (size > size_10000):
            lst_100000.append(n)
        else:
            lst_more.append(n)

    file_statistics = {
        size_100: len(lst_100),
        size_1000: len(lst_1000),
        size_10000: len(lst_10000),
        size_100000: len(lst_100000),
        "more": len(lst_more)
    }
    for key, val in file_statistics.items():
        print("{}: {}".format(key, val))
