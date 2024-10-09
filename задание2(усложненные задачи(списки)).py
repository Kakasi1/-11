import random
numbers = [random.randint(1, 100) for _ in range(10)]

print("Список случайных чисел:", numbers)

count = {}

for number in numbers:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

max_count = max(count.values())
print("Максимальное количество одинаковых элементов:", max_count)
