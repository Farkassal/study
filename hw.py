phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

def first(phrase_1,phrase_2):
	if len(phrase_1) > len(phrase_2):
		print("Фраза 1 длиннее фразы 2")
	else:
		if len(phrase_1) < len(phrase_2):
			print("Фраза 2 длиннее фразы 1")
		else:
			print("Фразы равной длины")

def second():
	print("Введите год: ")
	year = input()
	if int(year)%4 == 0:
		print ("Високосный год")
	else:
		print ("Обычный год")

def zodiak():
	znak = ""
	print("Введите день: ")
	day = input()
	print("Введите месяц: ")
	month = input()
	if ((month=="Январь" and int(day)>=20) or (month=="Февраль" and int(day)<=18)):
		znak = "Водолей"
	else:
		if ((month=="Февраль" and int(day)>=19) or (month=="Март" and int(day)<=20)):
			znak = "Рыбы"
		else:
			if ((month=="Март" and int(day)>=21) or (month=="Апрель" and int(day)<=19)):
				znak = "Овен"
			else:
				if ((month=="Апрель" and int(day)>=20) or (month=="Май" and int(day)<=20)):
					znak = "Телец"
				else:
					if ((month=="Май" and int(day)>=21) or (month=="Июнь" and int(day)<=21)):
						znak = "Близнецы"
					else:
						if ((month=="Июнь" and int(day)>=22) or (month=="Июль" and int(day)<=22)):
							znak = "Рак"
						else:
							if ((month=="Июль" and int(day)>=23) or (month=="Август" and int(day)<=22)):
								znak = "Лев"
							else:
								if ((month=="Август" and int(day)>=23) or (month=="Сентябрь" and int(day)<=22)):
									znak = "Дева"
								else:
									if ((month=="Сентябрь" and int(day)>=23) or (month=="Октябрь" and int(day)<=22)):
										znak = "Весы"
									else:
										if ((month=="Октябрь" and int(day)>=23) or (month=="Ноябрь" and int(day)<=21)):
											znak = "Скорпион"
										else:
											if ((month=="Ноябрь" and int(day)>=22) or (month=="Декабрь" and int(day)<=21)):
												znak = "Стрелец"
											else:
												if ((month=="Декабрь" and int(day)>=22) or (month=="Январь" and int(day)<=19)):
													znak = "Козерог"
												else:
													znak = "Неверная дата!"
	return print("Ваш знак задиака: " + znak)

def isin():
	print("Введите ширину: ")
	width = input()
	print("Введите длину: ")
	length = input()
	print("Введите высоту: ")
	height = input()
	if (int(width)<= 15 and int(length) <=15 and int(height) <= 15):
		return print("Коробка №1")
	elif (int(width)>200 or int(length)>200 or int(height)>200):
		return print("Упаковка для лыж")
	elif ((int(width)>15 and int(width)<50) or (int(length)>15 and int(length)<50) or (int(width)>15 and int(length)<50)):
		return print("Коробка №2")
	else:
		return print("Коробка №3")


def main():
	end = True
	while end:		
		print("\n\nВыберите задание: \nЗадание 1 - 1\nЗадание 2 - 2\nЗадание 3 - 3\nЗадание 4 - 4\nЗавершить - 5")
		n = input()
		if n == "1":
			first(phrase_1,phrase_2)
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