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


#Playfair Cipher.....DONE
class Playfair():
    def __init__(self, key):
        self.key = str(key)
        self.symbols = string.ascii_lowercase
        self.symbols = list(self.symbols)

    def removeUnique(self):
        # handle the case of i/j being the same
        if 'i' in self.key:
            self.symbols.remove('j')
        if 'j' in self.key:
            self.symbols.remove('i')
        if 'i' and 'j' in self.symbols:
            self.symbols.remove('j')
        alphabet = ''.join(self.symbols)
        self.string = self.key + alphabet
        self.string = list(self.string)
        output = []
        seen = set()
        for char in self.string:
            if char not in seen:
                output.append(char)
                seen.add(char)

        return output

    def createMatrix(self):
        self.string = self.removeUnique()
        #create 5x5 matrix
        matrix = []
        i = 0
        while i < 25:
            matrix.append(self.string[i:i+5])
            i += 5
        return matrix

    def createPairs(self, plainText):
        self.plainText = plainText.lower()
        self.plainText = plainText.replace(' ','')
        pairs = []
        self.plainText = list(self.plainText)

        i = 0
        while i < len(self.plainText) - 1:
            if self.plainText[i + 1] == self.plainText[i]:
                self.plainText.insert(i + 1, 'x')
                i += 2
            else:
                i += 1
        pairs = [self.plainText[i:i + 2] for i in xrange(0, len(self.plainText), 2)]
        if len(pairs[len(pairs) - 1]) == 1:
            pairs[len(pairs) - 1].append('x')
        return pairs

    def encrypt(self, plainText):
        self.pairs = self.createPairs(plainText)
        self.matrix = self.createMatrix()

        pairs = self.pairs
        matrix = self.matrix

        print pairs
        print matrix

        cipherText = []
        value1 = 0
        value2 = 0
        temp_list1 = []
        temp_list2 = []

        for pair in self.pairs:
            for row in matrix:
                if pair[0] in row:
                    temp_list1 = row
                if pair[1] in row:
                    temp_list2 = row
            for index in range(len(temp_list1)):
                if pair[0] == temp_list1[index]:
                    value1 = index
            for index in range(len(temp_list2)):
                if pair[1] == temp_list2[index]:
                    value2 = index

            # what if they are in the same row
            if temp_list1 == temp_list2:
                if value1 != 4: # move one to the right
                    value1 += 1
                else:
                    value1 = 0
                if value2 != 4:
                    value2 += 1
                else:
                    value2 = 0

            # what if they are in the same column
            if value1 == value2:
                index = 0
                while index < len(matrix):
                    if temp_list1 == matrix[index]:
                        if index == 0:
                            temp_list1 = matrix[4]
                        else:
                            index -= 1
                            temp_list1 = matrix[index]
                    if temp_list2 == matrix[index]:
                        if index == 0:
                            temp_list2 = matrix[4]
                        else:
                            index -= 1
                            temp_list2 == matrix[index]
                    index += 1


            cipherText += temp_list1[value2]
            cipherText += temp_list2[value1]

        return ''.join(cipherText)


    def decrypt(self, cipherText):
        self.pairs = self.createPairs(cipherText)
        self.matrix = self.createMatrix()

        pairs = self.pairs
        matrix = self.matrix

        plainText = []
        value1 = 0
        value2 = 0
        temp_list1 = []
        temp_list2 = []

        for pair in self.pairs:
            for row in matrix:
                if pair[0] in row:
                    temp_list1 = row
                if pair[1] in row:
                    temp_list2 = row
            for index in range(len(temp_list1)):
                if pair[0] == temp_list1[index]:
                    value1 = index
            for index in range(len(temp_list2)):
                if pair[1] == temp_list2[index]:
                    value2 = index

            # what if they are in the same row
            if temp_list1 == temp_list2:
                if value1 != 0: # move one to the left
                    value1 -= 1
                else:
                    value1 = 4
                if value2 != 0:
                    value2 -= 1
                else:
                    value2 = 4

            # what if they are in the same column
            if value1 == value2:
                index = 0 # go below one
                while index < len(matrix):
                    if temp_list1 == matrix[index]:
                        if index == 4:
                            temp_list1 = matrix[0]
                        else:
                            index += 1
                            temp_list1 = matrix[index]
                    if temp_list2 == matrix[index]:
                        if index == 4:
                            temp_list2 = matrix[0]
                        else:
                            index += 1
                            temp_list2 == matrix[index]
                    index += 1

            plainText += temp_list1[value2]
            plainText += temp_list2[value1]

        return ''.join(plainText)

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
            print table
        for i in range(len(table)):
            cipherText += table[i]
        return cipherText

    def decrypt(self, cipherText):
        self.cipherText = cipherText
        value = len(self.cipherText)%self.key
        # base amount of rows
        row_length = len(self.cipherText)/self.key
        print len(self.cipherText)
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

        print table
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

def main():
    # for caesar cipher
    symbols = string.ascii_lowercase

    sample = Playfair('monarchy')
    plainText = 'hello world'
    cipherText = sample.encrypt(plainText)
    sample.decrypt(cipherText)


if __name__=='__main__':
    main()
