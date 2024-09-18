N = int(input("Введите число N: "))
s = 0.0
for i in range(1, N + 1):
    s += 1 / i
print("Сумма чисел от 1 до 1/N равна:",s)
