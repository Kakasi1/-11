x = float(input("Введите значение x: "))
n = int(input("Введите количество членов n: "))
total_sum = 0.0

for i in range(n):
    total_sum += 1 / (x ** (2 * i))
print("Сумма первых", n, "членов ряда равна:", total_sum)
