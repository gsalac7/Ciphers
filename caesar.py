import string
import CipherInterface
#Caesar cipher... done
class Caesar():
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = int(key)

    def encrypt(self, plainText):
        self.plainText = plainText.replace(' ','')
        self.plainText = self.plainText.lower()
        cipherText = ''
        for char in self.plainText:
            num = ord(char)
            num += self.key
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26
            cipherText += chr(num)
        cipherText = cipherText[0:len(cipherText)-1]
        return cipherText

    def decrypt(self, cipherText):
        self.cipherText = cipherText.replace(' ','')
        plainText = ''
        key = -self.key
        for char in self.cipherText:
            num = ord(char)
            num += key
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26
            plainText += chr(num)
        return plainText
