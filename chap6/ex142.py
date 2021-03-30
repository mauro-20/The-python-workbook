# Unique Characters

def unique_characters(text: str):
    characters = {}
    for ch in text:
        characters[ch] = 'ok'

    print('"{}" has {} unique characters'.format(text, len(characters)))


def main():
    text = input('enter a string: ')
    unique_characters(text)


if __name__ == '__main__':
    main()
