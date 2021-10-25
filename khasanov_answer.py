from utils import currency_rates as c_r
import sys

# это файл с 5 заданием, назван khasanov_answer для удобства вызова
if __name__ == '__main__':
    argument_word = sys.argv[1]
    c_r(argument_word)
