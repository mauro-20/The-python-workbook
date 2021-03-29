# Word by Word Palindromes

from ex117 import words_of_string


# determine is a string is a word by word palindrome
# @param t is the string to execute
# @return True is the string is a word by word palindrome, False otherwise
def is_word_palindrome(t):
    # create a list of words without punctuation
    word_list = words_of_string(t)
    # compute if the list is palindrome
    isPalindrome = True
    if word_list:
        i = 0
        while i < len(word_list) / 2 and isPalindrome:
            if word_list[i] != word_list[len(word_list) - 1 - i]:
                isPalindrome = False
            i += 1
    return isPalindrome


# test is_word_palindrome() from user input
def main():
    t = input('enter a string: ')
    if is_word_palindrome(t):
        print("it's a word by word palindrome")
    else:
        print("it's not a word by word palindrome")


if __name__ == '__main__':
    main()
