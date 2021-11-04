import sys

if __name__ == "__main__":
    # Проверка аргументов
    if len(sys.argv) == 3:
        start, end = sys.argv[1], sys.argv[2]
        start = int(start)
        end = int(end)
    elif len(sys.argv) == 2:
        start = sys.argv[1]
        end = ""
        start = int(start)
    else:
        start, end = "", ""
    condition = len(sys.argv)
    i = 1

    with open("bakery.csv", "r", encoding="utf-8") as f:
        if condition == 3:
            for line in f:
                content_line = line.replace("\ufeff", "").replace('\n', '')
                if (i >= start) and (i <= end):
                    print(content_line)
                i += 1
        elif condition == 2:
            for line in f:
                content_line = line.replace("\ufeff", "").replace('\n', '')
                if i >= start:
                    print(content_line)
                i += 1
        else:
            for line in f:
                content_line = line.replace("\ufeff", "").replace('\n', '')
                print(content_line)
