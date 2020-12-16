# Is a String a Palindrome?

string = input('enter a string: ')

isPalindrome = True
if string:
    i = 0
    while i < len(string) / 2 and isPalindrome:
        if string[i] != string[len(string)-1-i]:
            isPalindrome = False
        i += 1

if isPalindrome:
    print(string, 'is palindrome')
else:
    print(string, 'is not palindrome')
