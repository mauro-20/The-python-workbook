# MultipleWord Palindromes

import string

punctuation = string.punctuation
string_in = input('enter a string: ')

# remove spaces
string_in = string_in.replace(' ', '')

# remove punctuation marks
no_punctuation = ''
for i in string_in:
    if i not in punctuation:
        no_punctuation += i
string_in = no_punctuation

isPalindrome = True
if string_in:
    i = 0
    while i < len(string_in) / 2 and isPalindrome:
        if string_in.lower()[i] != string_in.lower()[len(string_in)-1-i]:
            isPalindrome = False
        i += 1

if isPalindrome:
    print(string_in, 'is palindrome')
else:
    print(string_in, 'is not palindrome')
