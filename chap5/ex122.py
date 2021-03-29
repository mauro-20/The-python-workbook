# Pig Latin

# transforms english word in pig latin
# @param word is the word to be translated
# @return pig latin word
def pig_latin(word):

    # init
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    # transform the word string in a list
    l_word = list(word.lower())

    # transform english word in pig latin
    word_end = []
    if l_word[0] in consonants:
        while l_word[0] in consonants:
            word_end.append(l_word.pop(0))
        return ''.join(l_word + word_end + ['ay'])
    elif l_word[0] in vowels:
        return ''.join(l_word + ['way'])


def main():
    word = input('enter a word: ')
    print(pig_latin(word))


if __name__ == '__main__':
    main()
