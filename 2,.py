number1 = int(input("Введите первое число:  "))
number2 = int(input("Введите второе число:  "))

if number2 != 0:
    if number1 % number2 == 0:
        print(f"{number1} кратно {number2}")
    else:
        print(f"{number1} не кратно {number2}")
else:
    print("На ноль делить нельзя.")
