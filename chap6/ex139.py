# Morse Code

# transform text to morse code
# @param text the text to be transformed
# @return a string of morse code corresponding to the text
def text_to_morse(text):
    let2morse = {'A': '.-', 'B': '-...','C': '-.-.', 'D': '-..', 'E': '.',
                 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                 '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                 '9': '----.'}
    result = ''
    text = text.upper()
    for ch in text:
        if ch in let2morse:
            result += let2morse[ch]
            result += ' '
    return result


# testing text_to_morse()
print(text_to_morse('hello word'))
