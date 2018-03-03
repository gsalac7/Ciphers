import string

#Caesar cipher... done
class Caesar():
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = int(key)

    def encrypt(self, plainText):
        plainText = plainText.replace(' ','')
        cipherText = self.alphabet[self.key:] + self.alphabet[:self.key]
        table = string.maketrans(self.alphabet, cipherText)
        cipherText = plainText.translate(table)
        return cipherText

    def decrypt(self, cipherText):
        key = -self.key
        plainText = self.alphabet[key:] + self.alphabet[:key]
        table = string.maketrans(self.alphabet, plainText)
        plainText = cipherText.translate(table)
        return plainText


#TODO start on playfair cipher
class Playfair():
    def __init__(self, key):
        self.key = str(key)
        self.symbols = string.ascii_lowercase


    def removeUnique(self, string):
        remove = list(string)
        for char in range(len(remove) - 1):
            i = 1
            while i <= (len(remove) - 1):
                if remove[char] == remove[i]:
                    del remove[i]
                i += 1

        return str(remove)
    #makes the matrix based on the key
    def makeMatrix(self):
        matrix = self.key
        matrix = self.removeUnique(matrix)
        for characters in self.symbols:
            # we will just ignore j
            if characters == 'j':
                continue
            if characters not in matrix:
                matrix += characters

        list(matrix)
        print matrix
        matrix1 = matrix[0:5]
        matrix2 = matrix[6:10]
        matrix3 = matrix[11:15]
        matrix4 = matrix[16:20]
        matrix5 = matrix[21:25]
        print matrix1
        print matrix2
        print matrix3
        print matrix4
        print matrix5


    # the text can be both the ciphertext and the plaintext
    def createPairs(self, text):
        text = text.lower()
        text = text.replace(' ','')
        pairs = []
        i = 0;
        while i < len(text) - 1:
            if text[i] != text[i+1]:
                pairs.append((text[i], text[i+1]))
                i += 2
            else:
                pairs.append((text[i], 'x'))
                i += 1
        print pairs

    def encryptPair(self, pair):
        print 'SOMETHING'

#TODO start on vigenere cipher
class Vigenere():
    def __init__(self, key):
        self.key = int(key)

    def encrypt(self, plainText):
        print 'something'


    def decrypt(self, cipherText):
        print 'something '

# Row Transposition Done
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

#TODO decrypt function, encrypt works
class RailFence():
    def __init__(self, key):
        self.key = int(key)

    def encrypt(self, plainText):
        self.plainText = plainText.lower()
        self.plainText = self.plainText.replace(' ','')
        table = []
        for i in range(self.key):
            table.append('')
        i = 0
        while i < len(self.plainText):
            table[i % self.key] += self.plainText[i]
            i += 1
        cipherText = ''.join(table)
        return cipherText

    def decrypt(self, cipherText):
        self.cipherText = cipherText
        value = len(self.cipherText)%self.key
        # the amount of rows
        row_length = len(self.cipherText)/self.key

        row_start = 0
        table = []

        if value == 0:
            while value != 0:
                row_end = row_length + 1
                for i in range(self.key):
                    table.append('')
                    table[i] = self.cipherText[row_start:row_end]
                    row_start = row_end
                    row_end += row_length
                value -= 1
        else:
            row_end = row_length + value
            for i in range(self.key):
                table.append('')
                table[i] = self.cipherText[row_start:row_end]
                row_start = row_end
                row_end += row_length

        print table

        '''
        i = 0
        plainText = ''
        while len(plainText) != len(self.cipherText):
            for item in table:
                if i < len(item):
                    plainText += table[i]
            i += 1
        '''
        #return plaintext

def main():
    # for caesar cipher
    symbols = string.ascii_lowercase

    sample = RailFence(3)
    plainText = 'hello worlds'
    cipherText = sample.encrypt(plainText)
    print cipherText
    sample.decrypt(cipherText)


if __name__=='__main__':
    main()
