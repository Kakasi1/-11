import random

numbers = [random.randint(1, 100) for _ in range(10)]

print("Список случайных чисел:", numbers)
max_number = max(numbers)
sum_of_numbers = sum(numbers)  # Суммируем элементы списка

print("Наибольшее число в списке:", max_number)
print("Сумма чисел в списке:", sum_of_numbers)