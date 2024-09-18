N = int(input("Введите число N: "))

s = 0

for i in range(N + 1):
    s += 1 + (i / 10)

print("Сумма чисел от 1 до (1 + 1.1 + N / 10) равна:",s )




