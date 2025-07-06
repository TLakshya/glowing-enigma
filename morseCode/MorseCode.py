morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',  'J': '.---',
    'K': '-.-', 'L': '.-..','M': '--',  'N': '-.',  'O': '---',
    'P': '.--.','Q': '--.-','R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-','W': '.--', 'X': '-..-','Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---','3': '...--','4': '....-',
    '5': '.....', '6': '-....', '7': '--...','8': '---..','9': '----.'
}

def text_to_morse(text):
    text = text.upper()
    morse_code = ''
    for char in text:
        if char == ' ':
            morse_code += ' / '
        elif char in morse_dict:
            morse_code += morse_dict[char] + ' '
    return morse_code.strip()

u_input = input("Enter text to convert to Morse code: ")
print("Morse code:", text_to_morse(u_input))