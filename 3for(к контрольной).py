n = int(input("Введите количество чисел (n): "))

even_count = 0
odd_count = 0

for i in range(n):
    number = int(input(f"Введите число {i + 1}: "))


    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Количество четных чисел:", even_count)
print("Количество нечетных чисел:", odd_count)