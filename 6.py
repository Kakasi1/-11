number = int(input("Введите целое число:  "))

if number < 0:
    if number % 2 == 0:
        print = ("отрицательное четное число")
    else:
        print = ("отрицательное нечетное число")
elif number == 0:
    print = ("ноль")
else:
    if number % 2 == 0:
        print = ("положительное четное число")
    else:
         print = ("положительное нечетное число")