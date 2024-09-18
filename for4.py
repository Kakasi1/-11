K = int(input("Введите число K: "))
N = int(input("Введите число N: "))

if K % 2 == 1:
 K += 1

summ = 0
for i in range(K, N + 1,2):

 summ += i
print(f"сумма четных от K до N: {summ}")
