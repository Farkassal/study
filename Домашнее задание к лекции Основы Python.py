phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'


def first(phrase_1, phrase_2):
    if len(phrase_1) > len(phrase_2):
        print("Фраза 1 длиннее фразы 2")
    elif len(phrase_1) < len(phrase_2):
        print("Фраза 2 длиннее фразы 1")
    else:
        print("Фразы равной длины")


def second():
    year = input("Введите год: ")
    if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
        print("Високосный год")
    else:
        print("Обычный год")


def zodiak():
    day = input("Введите день: ")
    month = input("Введите месяц: ")
    if ((month == "Январь" and int(day) >= 20) or (month == "Февраль" and int(day) <= 18)):
        sign = "Водолей"
    elif ((month == "Февраль" and int(day) >= 19) or (month == "Март" and int(day) <= 20)):
        sign = "Рыбы"
    elif ((month == "Март" and int(day) >= 21) or (month == "Апрель" and int(day) <= 19)):
        sign = "Овен"
    elif ((month == "Апрель" and int(day) >= 20) or (month == "Май" and int(day) <= 20)):
        sign = "Телец"
    elif ((month == "Май" and int(day) >= 21) or (month == "Июнь" and int(day) <= 21)):
        sign = "Близнецы"
    elif ((month == "Июнь" and int(day) >= 22) or (month == "Июль" and int(day) <= 22)):
        sign = "Рак"
    elif ((month == "Июль" and int(day) >= 23) or (month == "Август" and int(day) <= 22)):
        sign = "Лев"
    elif ((month == "Август" and int(day) >= 23) or (month == "Сентябрь" and int(day) <= 22)):
        sign = "Дева"
    elif ((month == "Сентябрь" and int(day) >= 23) or (month == "Октябрь" and int(day) <= 22)):
        sign = "Весы"
    elif ((month == "Октябрь" and int(day) >= 23) or (month == "Ноябрь" and int(day) <= 21)):
        sign = "Скорпион"
    elif ((month == "Ноябрь" and int(day) >= 22) or (month == "Декабрь" and int(day) <= 21)):
        sign = "Стрелец"
    elif ((month == "Декабрь" and int(day) >= 22) or (month == "Январь" and int(day) <= 19)):
        sign = "Козерог"
    else:
        sign = "Неверная дата!"
    return print("Ваш знак задиака: " + sign)


def isin():
    width = input("Введите ширину: ")
    length = input("Введите длину: ")
    height = input("Введите высоту: ")
    if (int(width) <= 15 and int(length) <= 15 and int(height) <= 15):
        return print("Коробка №1")
    elif (int(width) > 200 or int(length) > 200 or int(height) > 200):
        return print("Упаковка для лыж")
    elif ((int(width) > 15 and int(width) < 50) or (int(length) > 15 and int(length) < 50) or (
            int(width) > 15 and int(length) < 50)):
        return print("Коробка №2")
    else:
        return print("Коробка №3")


def main():
    end = True
    while end:
        print("\n\nВыберите задание: \nЗадание 1 - 1\nЗадание 2 - 2\nЗадание 3 - 3\nЗадание 4 - 4\nЗавершить - 5")
        n = input()
        if n == "1":
            first(phrase_1, phrase_2)
        elif n == "2":
            second()
        elif n == "3":
            zodiak()
        elif n == "4":
            isin()
        elif n == "5":
            end = False
        else:
            print("Неврная команда!")


if __name__ == '__main__':
    main()
