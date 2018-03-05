import string
import re
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
        # handle the final one, make sure it's not alone...has an x
        if len(pairs[len(pairs) - 1]) == 1:
            pairs[len(pairs) - 1].append('x')
        return pairs

    def encrypt(self, plainText):
        self.pairs = self.createPairs(plainText)
        self.matrix = self.createMatrix()

        pairs = self.pairs
        matrix = self.matrix
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
                index = 0 # go up one
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
                            temp_list2 = matrix[index]
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

        plainText = ''.join(plainText)
        return plainText
