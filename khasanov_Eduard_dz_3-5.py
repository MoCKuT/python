from random import choice


def get_jokes(nouns, adverbs, adjectives, indication: int, replay_word="Yes"):
    """

    :param nouns:list_one
    :param adverbs:list_two
    :param adjectives:list_three
    :param indication: number of offers
    :param replay_word: "Yes" or "No" repeat words
    """
    replay, replay_yes, bool_replay = replay_word, "Yes", True
    space, i, n = ' ', 1, ''
    joke_lst = []
    joke_lst_str = ''
    n = sorted([len(nouns), len(adverbs), len(adjectives)])

    while i <= indication:
        nouns_element = choice(nouns)
        adverbs_element = choice(adverbs)
        adjectives_element = choice(adjectives)
        # Повторов не будет только в том случае, если переменная replay_word="Yes".
        # А так же, если количество предложений указанно меньше, чем длинна самого короткого из указанных списков,
        # это сделано во избежание зацикливаний функции
        if replay != replay_yes and indication < n[0]:
            while nouns_element in joke_lst_str != bool_replay:
                nouns_element = choice(nouns)

            while adverbs_element in joke_lst_str != bool_replay:
                adverbs_element = choice(adverbs)

            while adjectives_element in joke_lst_str != bool_replay:
                adjectives_element = choice(adjectives)
        else:
            pass

        joke_str = nouns_element + space + adverbs_element + space + adjectives_element
        joke_lst_str = joke_lst_str + joke_str + space
        joke_lst.append(joke_str)
        i += 1
    return joke_lst


lst_one = ["автомобиль", "лес", "огонь", "город", "дом"]
lst_two = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
lst_three = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(lst_one, lst_two, lst_three, 2, replay_word="No"))
