K =int(input("Введите число K = "))
N =int(input("Введите число N = "))
sum_numbers = 0
for i in range(K , N + 1):
    if i % 2 == 0:
        sum_numbers += i
print(sum_numbers)