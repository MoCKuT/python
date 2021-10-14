
# Выводит минуты, часы, дни при наличии

in_time = int(input("duration: "))

integer_minute = in_time // 60 + 0
integer_hours = integer_minute // 60
integer_day = integer_hours // 24

remainder_second = in_time % 60
remainder_minute = integer_minute % 60
remainder_hours = integer_hours % 24

second = str(remainder_second) + " сек."
minute = ""
hours = ""
day = ""

if integer_minute > 0:
    minute = str(remainder_minute) + " мин."
    if integer_hours > 0:
        hours = str(remainder_hours) + " ч."
        if integer_day > 0:
            day = str(integer_day) + " дн."
        else:
            pass
    else:
        pass
else:
    pass

print(day, hours, minute, second)
