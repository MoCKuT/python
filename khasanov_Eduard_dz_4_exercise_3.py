import requests
from datetime import datetime
from decimal import Decimal


def currency_rates(input_name: str):
    data_http, data_out, data_edit = "", "", ""
    currency, currency_value, word = "", "", ""
    out_function = ""
    indication_date, indication, i = 0, 1, 1

    # Редактирую полученный с сайта текст
    result = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    result_edit = ('\n'.join(result.text.split("Valute ID=")))
    result_edit = (' '.join(result_edit.split("<")))
    result_edit = result_edit.replace(">", " ")
    result_edit = result_edit.replace("/", "")
    result_edit = result_edit.replace("  ", " ")

    # Получаю дату
    while indication_date != len(result_edit):
        indication_date_start = indication_date + 1
        indication_date_end = indication_date + 11
        data_http = result_edit[indication_date]
        if data_http != " ":
            data_edit = data_edit + data_http
            if data_edit == 'Date="':
                data_out = result_edit[indication_date_start: indication_date_end]
                indication_date = len(result_edit) - 1
            else:
                pass
        else:
            data_edit = ""
        indication_date += 1

    # Привожу дату к классу Date
    date = datetime(year=int(data_out[6:]), month=int(data_out[3:5]), day=int(data_out[:2]))
    date = date.date()

    # Цикл поиска по тексту
    for name in result_edit:
        space = " "
        if name != space:
            word = word + name
            if word == "CharCode":
                indication += 1
            else:
                pass

            if word == "Value":
                i += 1
            else:
                pass

        else:
            if (indication % 2 == 0) and (word != "") and word != "CharCode":
                currency = word
            else:
                pass

            if (i % 2 == 0) and (word != "") and word != "Value":
                currency_value = Decimal(word[:5].replace(",", "."))
                # изменил переменную
                if input_name.upper() == currency:
                    out_function = currency_value
                else:
                    pass
            else:
                pass

            word = ""
    if out_function != "":
        return print(out_function, end=", "), print(date)
    else:
        return print(None)


currency_rates("usd"), currency_rates("Eur")
