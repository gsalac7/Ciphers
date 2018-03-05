import string
# vigenere done
class Vigenere():
    def __init__(self, key, symbols):
        self.key = key.lower()
        self.symbols = symbols

    def encrypt(self, plainText):
        self.plainText = plainText.lower()
        self.plainText = self.plainText.replace(' ','')
        keyIndex = 0
        cipherText = ''
        for char in self.plainText:
            num = self.symbols.find(char)
            num += self.symbols.find(self.key[keyIndex])

            if num > ord('z'):
                num += 26
            elif num < ord('a'):
                num -= 26

            cipherText += self.symbols[num]

            keyIndex += 1
            if keyIndex == len(self.key):
                keyIndex = 0

        return cipherText

    def decrypt(self, cipherText):
        self.cipherText = cipherText.lower()
        self.cipherText = self.cipherText.replace(' ','')
        keyIndex = 0
        plainText = ''
        for char in self.cipherText:
            num = self.symbols.find(char)
            num -= self.symbols.find(self.key[keyIndex])

            num %= len(self.symbols)

            plainText += self.symbols[num]

            keyIndex += 1
            if keyIndex == len(self.key):
                keyIndex = 0

        return plainText
