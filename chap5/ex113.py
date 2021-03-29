# Avoiding Duplicates

words = []

word = input('enter a word (blank to quit): ')
while word != '':
    if word not in words:
        words.append(word)
    word = input('enter a word (blank to quit): ')


for word in words:
    print(word)
