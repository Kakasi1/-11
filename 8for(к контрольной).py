num_segments = int(input("Введите количество участков: "))

total_time = 0.0

for i in range(num_segments):
    length = float(input(f"Введите длину участка {i + 1} (в км): "))
    speed = float(input(f"Введите среднюю скорость на участке {i + 1} (в км/ч): "))

    if speed > 0:
        time = length / speed
        total_time += time
    else:
        print("Скорость должна быть больше нуля.")
        break

if speed > 0:
    print(f"Общее время поездки: {total_time:.2f} часов")