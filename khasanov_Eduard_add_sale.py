import sys

if __name__ == "__main__":
    add_sum = str(sys.argv[1]) + "\n"
    with open("bakery.csv", "a", encoding="utf-8") as f:
        f.write(add_sum)
    print("___Строка добавлена___")
