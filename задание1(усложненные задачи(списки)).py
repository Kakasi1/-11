import random

numbers = [random.randint(1, 100) for _ in range(10)]

print("Список случайных чисел:", numbers)

last_local_max_index = -1

for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        last_local_max_index = i
if numbers[0] > numbers[1]:
    last_local_max_index = 0
if numbers[-1] > numbers[-2]:
    last_local_max_index = len(numbers) - 1

if last_local_max_index != -1:
    print("Номер последнего локального максимума:", last_local_max_index)
    print("Значение последнего локального максимума:", numbers[last_local_max_index])
else:
    print("Локальных максимумов в списке нет.")