n = int(input("Введите число n: "))

even_divisors = []

for i in range(1, n + 1):
    if n % i == 0 and i % 2 == 0:
        even_divisors.append(i)
if even_divisors:
    print("Четные делители числа", n, ":", even_divisors)
else:
    print("У числа", n, "нет четных делителей.")