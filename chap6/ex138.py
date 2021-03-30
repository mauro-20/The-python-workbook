# Text Messaging

# gives you the sequence of digit to write a text on an old type cellphone
# @param text the text to be transformed
# @return a string of the digits needed to be pressed to generate the text
def text_to_keypad(text: str):
    keypad = {1: ['.', ',', '?', '!', ':'],
              2: ['A', 'B', 'C'],
              3: ['D', 'E', 'F'],
              4: ['G', 'H', 'I'],
              5: ['J', 'K', 'L'],
              6: ['M', 'N', 'O'],
              7: ['P', 'Q', 'R', 'S'],
              8: ['T', 'U', 'V'],
              9: ['W', 'X', 'Y', 'Z'],
              0: [' ']}
    result = ''
    text = text.upper()
    for ch in text:
        for k in keypad:
            val = keypad[k]
            for el in val:
                if el == ch:
                    result += str(k)*(val.index(el)+1)
                    result += ' '
    return result


print(text_to_keypad('Hello Word!!'))
