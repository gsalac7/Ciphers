class CipherInterface():
    def setKey(self, key):
        self.key = key

    def Encrypt(self, plainText):
        return plainText

    def Decrypt(self, cipherText):
        return cipherText
