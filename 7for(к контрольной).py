n = int(input("Введите число n: "))

if n <= 0:
    print("Число должно быть положительным.")
else:

    print("Комбинации чисел от 1 до", n, ":")

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j != i:
                print(f"({i}, {j})")