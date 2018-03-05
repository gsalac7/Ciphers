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
        cipherText = self.alphabet[self.key:] + self.alphabet[:self.key]
        table = string.maketrans(self.alphabet, cipherText)
        cipherText = plainText.translate(table)
        return cipherText

    def decrypt(self, cipherText):
        self.cipherText = cipherText.replace(' ','')
        key = -self.key
        plainText = self.alphabet[key:] + self.alphabet[:key]
        table = string.maketrans(self.alphabet, plainText)
        plainText = cipherText.translate(table)
        return plainText
