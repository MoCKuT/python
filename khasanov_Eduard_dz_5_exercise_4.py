
# Задание 4
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src_len = int(len(src))

result = [src[i] for i in range(0, src_len) if (src[i - 1]) < src[i]]
if __name__ == '__main__':
    print(result)

