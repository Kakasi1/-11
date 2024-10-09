user_input = input("Введите строку: ")

char_list = list(user_input)

filtered_list = [char for char in char_list if char not in ('а', 'е', 'о')]
print("Итоговый список:", filtered_list)

result_string = ''.join(filtered_list)
print("Строка без символов 'а', 'е', 'о':", result_string)