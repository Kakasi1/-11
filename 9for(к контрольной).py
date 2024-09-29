initial_price = float(input("Введите исходную цену товара: "))
discount_increase = float(input("Введите размер увеличения скидки (в %): "))
num_items = int(input("Введите количество товаров для покупки: "))


remaining_money = 0.0

remaining_money = float(input("Введите сумму денег, которую у вас есть: "))


current_discount = 0.0

for i in range(num_items):
    current_price = initial_price * (1 - current_discount / 100)

    if remaining_money >= current_price:
        remaining_money -= current_price
        print(f"Куплен товар {i + 1} по цене {current_price:.2f} (скидка {current_discount:.2f}%)")
    else:
        print(f"Недостаточно средств для покупки товара {i + 1}.")
        break

    current_discount += discount_increase
print(f"Оставшиеся деньги: {remaining_money:.2f}")