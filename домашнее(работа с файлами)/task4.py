with open('story.txt', 'r') as infile:
    content = infile.read()

content = content.replace('Python', 'Java')

with open('new_story.txt', 'w') as outfile:
    outfile.write(content)
