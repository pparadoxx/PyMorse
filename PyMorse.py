DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    message = message.upper()
    cipher = ''
    for letter in message:
        if letter != ' ':
            # Look up the morse code for the letter
            cipher += DICT[letter] + ' '
        else:
            # Use a forward slash to separate words
            cipher += '/'

    return cipher

def decrypt(cipher):
    # Split the cipher into words
    words = cipher.split('/')
    decipher = ''
    for word in words:
        # Split the word into morse code letters
        letters = word.split()
        for letter in letters:
            # Look up the letter for the morse code
            decipher += list(DICT.keys())[list(DICT.values()).index(letter)]

        # Add a space between words
        decipher += ' '

    return decipher

def main():
    while True:
        choice = input("Would you like to encrypt or decrypt a message? (E/D): ")
        if choice == 'E':
            message = input("Enter the message to encrypt: ")
            result = encrypt(message.upper())
            print("Encrypted message: " + result)
        elif choice == 'D':
            message = input("Enter the message to decrypt: ")
            result = decrypt(message)
            print("Decrypted message: " + result)
        elif choice == "X":
            print("Thank you!")
            exit()
        else:
            print("Invalid input. Try again.\nIf you'd like to exit use the input X.")
            main()

main()