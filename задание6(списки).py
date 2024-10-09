list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in list1:
    if item in list2:
        list2.remove(item)
print("Итоговый второй список:", list2)