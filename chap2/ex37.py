# Vowel or Consonant

letter = input('enter a letter of the alphabet: ')

if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
elif letter == 'y':
    print(letter, 'can sometimes be a vowel and sometimes be a consonant')
else:
    print(letter, 'is a consonant')
