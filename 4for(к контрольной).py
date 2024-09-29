initial_rate = float(input("Введите курс на первый день: "))
n = int(input("Введите количество дней для расчета: "))

current_rate = initial_rate

print("\nКурсы на последующие дни:")
for day in range(1, n + 1):
    percentage_change = float(input(f"Введите процент изменения для дня {day}: "))


    current_rate += current_rate * (percentage_change / 100)

    print(f"Курс на день {day}: {current_rate:.2f}")