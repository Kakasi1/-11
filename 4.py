a = int(input("Введите время в часах:  "))

if 5 <= a <= 11:
    print("Утро")
elif 12 <= a <= 17:
    print("День")
elif 18 <= a <= 22:
    print("Вечер")
elif a >= 23 or a <= 4:
    print("Ночь")
else:
    print("Ошибка")
