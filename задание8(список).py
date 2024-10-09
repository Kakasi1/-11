import random

numbers = [random.randint(1, 100) for _ in range(10)]

print("Список случайных чисел:",numbers)
min_number = min(numbers)

print("Наибольшее число в списке:", min_number)