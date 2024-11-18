with open('text.txt') as file:
    lines = file.readlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)

print("Количество строк:", line_count)
print("Количество слов:", word_count)
