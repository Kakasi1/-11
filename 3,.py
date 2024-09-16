def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


a = float(input("Введите длину стороны a:  "))
b = float(input("Введите длину стороны b:  "))
c = float(input("Введите длину стороны c:  "))

if is_triangle(a, b, c):
    print("Треугольник существует.")
else:
    print("Треугольник не существует.")
