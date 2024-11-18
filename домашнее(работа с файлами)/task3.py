with open('input.txt') as infile, open('output.txt', 'w') as outfile:
    outfile.write(infile.read().upper())
