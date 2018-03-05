 #Row Transposition Done
class Transposition():
    def __init__(self, key):
        self.key = str(key)

    def encrypt(self, plainText):
        self.plainText = plainText.lower()
        self.plainText = self.plainText.replace(' ','')
        col = len(self.key)
        #start setting the table of the plainText
        table = []
        key = []
        for i in range(col):
            key.append(int(self.key[i]))

        for i in range(col):
            table.append('')

        # table is going to be a list of strings, where each string is a column
        i = 0
        j = 0
        while i < len(self.plainText):
            if j == col:
                j = 0
            table[j] += self.plainText[i]
            j += 1
            i += 1

        # add the remaining ones with x
        len_first = len(table[0])
        for item in range(len(table)):
            if len(table[item]) != len_first:
                table[item] += 'x'

        cipherText = ''
        # start assembling the CipherText
        for item in key:
            cipherText += table[item - 1]
        return cipherText


    def decrypt(self, cipherText):
        self.cipherText = cipherText
        row_length = len(self.cipherText)/len(self.key)
        table = []
        col_length = len(self.key)
        newTable = []

        key = []
        for i in range(col_length):
            key.append(int(self.key[i]))

        #divide the list evenly
        for i in range(col_length):
            table.append('')
            newTable.append('')

        table = [self.cipherText[i:i+row_length] for i in range(0, len(self.cipherText), row_length)]
        #print key
        #zprint table
        for i in range(len(key)):
            newTable[key[i] - 1] = table[i]

        plainText = ''
        j = 0
        while len(plainText) != len(self.cipherText):
            for i in range(len(newTable)):
                plainText += newTable[i][j]
            j += 1

        return plainText
