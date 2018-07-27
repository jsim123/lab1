strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for i in range(len(strings)):   
    sentence=sentence+strings[i]+' '
print(sentence.strip())

print(' '.join(strings))
