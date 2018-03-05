import string
import sys
from caesar import Caesar
from railFence import RailFence
from transposition import Transposition
from vigenere import Vigenere
from playFair import Playfair

def main():
    symbols = string.ascii_lowercase

    # first argument is the cipher
    cipher = sys.argv[1]

    # second arugment is the key
    key = sys.argv[2]

    # 3rd argument is the encrypt/Decrypt
    mode = sys.argv[3]

    # 4th argument is the input text
    input_txt = sys.argv[4]

    # 5th arugment is the output text
    output_txt = sys.argv[5]

    plainText = ''
    cipherText = ''

    text = open(input_txt)
    if mode == 'encrypt':
        plainText = text.read()
    if mode == 'decrypt':
        cipherText = text.read()

    if cipher == 'caesar' or cipher == 'Caesar':
        caesar = Caesar(key, symbols)
        if mode == 'encrypt':
            cipherText = open(output_txt, 'w')
            cipherText.write(caesar.encrypt(plainText))
            cipherText.close()
        if mode == 'decrypt':
            plainText = open(output_txt, 'w')
            plainText.write(caesar.decrypt(cipherText))
            plainText.close()

    if cipher == 'playfair' or cipher == 'Playfair':
        playfair = Playfair(key)
        if mode == 'encrypt':
            cipherText = open(output_txt, 'w')
            cipherText.write(playfair.encrypt(plainText))
            cipherText.close()
        if mode == 'decrypt':
            plainText = open(output_txt, 'w')
            plainText.write(playfair.decrypt(cipherText))
            plainText.close()

    if cipher == 'vigenere' or cipher == 'Vigenere':
        vigenere = Vigenere(key, symbols)
        if mode == 'encrypt':
            cipherText = open(output_txt, 'w')
            cipherText.write(vigenere.encrypt(plainText))
            cipherText.close()
        if mode == 'decrypt':
            plainText = open(output_txt, 'w')
            plainText.write(vigenere.decrypt(cipherText))
            plainText.close()

    if cipher == 'transposition' or cipher == 'Transposition':
        transposition = Transposition(key)
        if mode == 'encrypt':
            cipherText = open(output_txt, 'w')
            cipherText.write(transposition.encrypt(plainText))
            cipherText.close()
        if mode == 'decrypt':
            plainText = open(output_txt, 'w')
            plainText.write(transposition.decrypt(cipherText))
            plainText.close()

    if cipher == 'railfence' or cipher == 'Railfence':
        rail = RailFence(key)
        if mode == 'encrypt':
            cipherText = open(output_txt, 'w')
            cipherText.write(rail.encrypt(plainText))
            cipherText.close()
        if mode == 'decrypt':
            plainText = open(output_txt, 'w')
            plainText.write(rail.decrypt(cipherText))
            plainText.close()

if __name__=='__main__':
    main()
