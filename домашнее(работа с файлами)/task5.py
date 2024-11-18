with open('part1.txt', 'r') as part1, open('part2.txt', 'r') as part2, open('full_text.txt', 'w') as full_text:
    full_text.write(part1.read() + '\n' + part2.read())

