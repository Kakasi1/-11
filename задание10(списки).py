import random

numbers = [random.randint(1, 100) for _ in range(10)]

print("Список случайных чисел:", numbers)
max_number = max(numbers)
average = sum(numbers) / len(numbers)

print("Наибольшее число в списке:", max_number)
print("Среднее арифметическое чисел в списке:", average)