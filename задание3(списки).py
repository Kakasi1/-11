import random

numbers = []
for _ in range(10):
    number = random.randint(1, 100)
    numbers.append(number)
for number in numbers:
    print(number)