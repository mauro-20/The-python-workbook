# Only the Words

# gives a list of all the words of a string without punctuations at the end of the word
# @param s string provided
# @return a list of the words in the string
def words_of_string(s):
    punctuations = [':', ',', '.', ';', '?', '!', '-', "'"]
    # split the words from the string
    words = s.split()
    # remove the punctuations
    for i in range(len(words)):
        word = words[i]
        while word[-1] in punctuations:
            word = word[:-1]
            words[i] = word
    return words


def main():
    string = input('enter a string: ')
    print(words_of_string(string))


if __name__ == '__main__':
    main()
