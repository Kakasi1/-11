import random

numbers = [random.randint(1, 100) for _ in range(10)]

print("Список случайных чисел:",numbers)
max_number = max(numbers)

print("Наибольшее число в списке:", max_number)