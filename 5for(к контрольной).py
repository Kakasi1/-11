n = int(input("Введите количество чисел (p): "))

total_sum = 0
total_product = 1

for i in range(n):
    number = float(input(f"Введите число {i + 1}: "))

    total_sum += number


    total_product *= number

if n > 0:
    average = total_sum / n
else:
    average = 0
print(f"Сумма всех чисел: {total_sum}")
print(f"Произведение всех чисел: {total_product}")
print(f"Среднее арифметическое: {average:.2f}")