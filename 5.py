day = int(input("Введите номер дня недели (1-7):  "))

if day == 6 or day == 7:
    print("Выходные")
elif 1 <= day <= 5:
    print("Будни")
else:
    print("ошибка")
