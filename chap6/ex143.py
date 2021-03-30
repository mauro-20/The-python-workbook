# Anagrams

def counts(s):
    count = {}
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return count


def anagram(string1, string2):
    ch1 = counts(string1)
    ch2 = counts(string2)

    is_anagram = False
    if ch1 == ch2:
        is_anagram = True
    return is_anagram


def main():
    string1 = input('enter the first word: ')
    string2 = input('enter the second word: ')
    if anagram(string1, string2):
        print('they are anagrams')
    else:
        print('sorry no anagram')


if __name__ == '__main__':
    main()
