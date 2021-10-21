def num_translate(dictionary, key_enter):
    # word - приводит к нижнему регистру для того, чтобы заглавная буква не приводила к None
    word = key_enter.lower()
    dictionary_uot = dictionary.get(word)
    if dictionary_uot is None:
        return None
    elif key_enter != word:
        return dictionary_uot.title()
    return dictionary_uot


numerals = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

print(num_translate(numerals, input("Enter the numbers in letters: ")))
