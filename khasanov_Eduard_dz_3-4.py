def thesaurus_adv(*name):
    people_adv = {}
    for n in name:
        initial = n[0]
        name_split = n.split()
        initial_last_name = name_split[1][0]
        if people_adv.get(initial_last_name) is not None:
            if people_adv[initial_last_name].get(initial) is not None:
                people_adv[initial_last_name][initial].append(n)
            else:
                people_adv[initial_last_name][initial] = [n]
        else:
            people_adv[initial_last_name] = {initial: [n]}
    return people_adv


people_print = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(people_print)
print()


# предлагаю такую сортировку
for key in sorted(people_print):
    print(key, ": ", end=" ")
    indication = 0
    for key_branch in sorted(people_print[key]):
        if indication == 0:
            print(key_branch, ":", people_print[key][key_branch],)
        else:
            print("    ", key_branch, ":", people_print[key][key_branch], )
        indication += 1
    print("")
