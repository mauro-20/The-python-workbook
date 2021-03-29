# Pig Latin Improved

# transforms english word in pig latin
# @param word is the word to be translated
# @return pig latin word
def pig_latin(word):

    # init
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    punctuation = [',', '.', '?', '!']

    # transform the word string in a list
    l_word = list(word.lower())

    # remove punctuation and store it in word_pun
    word_pun = []
    for e in l_word:
        while l_word[-1] in punctuation:
            word_pun.append(l_word.pop(-1))

    # transform english word in pig latin
    word_end = []
    if l_word[0] in consonants:
        while l_word[0] in consonants:
            word_end.append(l_word.pop(0))
        res = ''.join(l_word + word_end + ['ay'] + word_pun)
    elif l_word[0] in vowels:
        res = ''.join(l_word + ['way'] + word_pun)

    # capitalize if the original word was capitalized
    if word[0].isupper():
        res = res.capitalize()

    return res


def main():
    word = input('enter a word: ')
    print(pig_latin(word))


if __name__ == '__main__':
    main()
