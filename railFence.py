# RAIL FENCE....DONEZO
class RailFence():
    def __init__(self, key):
        self.key = int(key)

    def encrypt(self, plainText):
        self.plainText = plainText.lower()
        self.plainText = self.plainText.replace(' ','')
        cipherText = ''
        table = []
        for i in range(self.key):
            table.append('')
        for i in range(len(self.plainText)):
            table[i % self.key] += self.plainText[i]
        for i in range(len(table)):
            cipherText += table[i]
        return cipherText

    def decrypt(self, cipherText):
        self.cipherText = cipherText
        value = len(self.cipherText)%self.key
        # base amount of rows
        row_length = len(self.cipherText)/self.key
        row_start = 0
        table = []
        row_end = 0
        for i in range(self.key):
            if value > 0:
                row_end += row_length + 1
                value -= 1
            else:
                row_end += row_length
            table.append('')
            table[i] += self.cipherText[row_start:row_end]
            row_start = row_end

        # actually buid the plainText now
        plainText = ''
        j = 0
        while len(plainText) != len(self.cipherText):
            for i in range(len(table)):
                plainText += table[i][j]
                if len(plainText) == len(self.cipherText):
                    break
            j += 1

        return plainText
