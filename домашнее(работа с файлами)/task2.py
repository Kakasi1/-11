with open('data.txt') as infile, open('data_even_numbers.txt', 'w') as outfile:
    even_numbers = [num for num in map(int, infile.read().split()) if num % 2 == 0]
    outfile.write(' '.join(map(str, even_numbers)))
