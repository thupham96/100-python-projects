MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

MORSE_CODE_REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def encoder(user_input):
    user_input = user_input.upper()
    encoded_output = []
    for char in user_input:
        if char == " ":
            encoded_output.append("/")  # separate words
        elif char in MORSE_CODE_DICT:
            encoded_output.append(MORSE_CODE_DICT[char])
        else:
            encoded_output.append('?')  # unknown character
    return ' '.join(encoded_output)

def decoder(user_input):
    words = user_input.strip().split(' / ')
    decoded_output = []
    for word in words:
        chars = word.strip().split()
        decoded_word = ''
        for morse_char in chars:
            decoded_word += MORSE_CODE_REVERSE_DICT.get(morse_char, '?')
        decoded_output.append(decoded_word)
    return ' '.join(decoded_output)

print("Welcome to Morse Code Translator!")

continuing = True
while continuing:
    mode = input("Would you like to encode or decode? ").strip().lower()
    user_string = input("What string would you like to encode/decode? ").strip()

    if mode == "encode":
        output = encoder(user_string)
        print(f"The translated message is: {output}")
    elif mode == "decode":
        output = decoder(user_string)
        print(f"The translated message is: {output}")
    else:
        print("Your choice is invalid. Please enter either encode or decode.")

    again = input("Would you like to encode or decode another string? (y/n) ").strip().lower()
    if again != 'y':
        continuing = False
