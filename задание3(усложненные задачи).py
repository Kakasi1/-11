import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("Список случайных чисел:", numbers)
first_max = second_max = float('-inf')

for number in numbers:
    if number > first_max:
        second_max = first_max
        first_max = number
    elif first_max > number > second_max:
        second_max = number
if second_max == float('-inf'):
    print("Недостаточно уникальных элементов для нахождения второго максимума.")
else:
    print("Второй максимум:", second_max)