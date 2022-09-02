# Riya Patel AU2140214

class sparse_matrix:

    def __init__(self, r, c):
        self.MAX = 100
        self.data = [None for i in range(self.MAX)]
        for i in range(self.MAX):
            self.data[i] = [None for i in range(3)]

        self.row = r
        self.col = c

        self.len = 0
    def insert(self, r, c, val):
        if (r > self.row or c > self.col):
            print("Wrong entry")
        else:
            self.data[self.len][0] = r
            self.data[self.len][1] = c
            self.data[self.len][2] = val
            self.len += 1
    def scaleBy(self,scalar):
        for i in range(self.len):
            self.data[i][2]=self.data[i][2]*scalar
        print(self.data)

    def getitem (self,row,col):
        if (row > self.row or col > self.col):
            print("Wrong entry")
        else:
            print('')


    def add(self, b):
        if (self.row != b.row or self.col != b.col):
            print("Matrices can't be added")
        else:

            apos = 0
            bpos = 0
            result = sparse_matrix(self.row, self.col)

            while (apos < self.len and bpos < b.len):
                if (self.data[apos][0] > b.data[bpos][0] or (
                        self.data[apos][0] == b.data[bpos][0] and self.data[apos][1] > b.data[bpos][1])):

                    result.insert(b.data[bpos][0],
                                  b.data[bpos][1],
                                  b.data[bpos][2])
                    bpos += 1

                elif (self.data[apos][0] < b.data[bpos][0] or (
                        self.data[apos][0] == b.data[bpos][0] and self.data[apos][1] < b.data[bpos][1])):

                    result.insert(self.data[apos][0], self.data[apos][1], self.data[apos][2])
                    apos += 1

                else:
                    addedval = self.data[apos][2] + b.data[bpos][2]

                    if (addedval != 0):
                        result.insert(self.data[apos][0], self.data[apos][1], addedval)
                    apos += 1
                    bpos += 1

            while (apos < self.len):
                result.insert(self.data[apos][0], self.data[apos][1], self.data[apos][2])
                apos += 1

            while (bpos < b.len):
                result.insert(b.data[bpos][0], b.data[bpos][1], b.data[bpos][2])
                bpos += 1
            result.print()

    def transpose(self):

        result = sparse_matrix(self.col, self.row)
        result.len = self.len
        count = [None for _ in range(self.col + 1)]
        for i in range(1, 1 + self.col):
            count[i] = 0

        for i in range(0, self.len):
            count[self.data[i][1]] += 1

        index = [None for _ in range(self.col + 1)]
        index[1] = 0
        for i in range(2, 1 + self.col):
            index[i] = index[i - 1] + count[i - 1]

        for i in range(self.len):
            rpos = index[self.data[i][1]]
            index[self.data[i][1]] += 1
            result.data[rpos][0] = self.data[i][1]
            result.data[rpos][1] = self.data[i][0]
            result.data[rpos][2] = self.data[i][2]

        return result

    def multiply(self, b):
        if (self.col != b.row):

            print("Can't multiply, Invalid dimensions")
            return

        b = b.transpose()

        result = sparse_matrix(self.row, b.row)

        for apos in range(self.len):

            r = self.data[apos][0]

            for bpos in range(b.len):

                c = b.data[bpos][0]

                tempa = apos
                tempb = bpos
                sum = 0

                while (tempa < self.len and self.data[tempa][0] == r and tempb < b.len and b.data[tempb][0] == c):

                    if (self.data[tempa][1] < b.data[tempb][1]):
                        tempa += 1

                    elif (self.data[tempa][1] > b.data[tempb][1]):
                        tempb += 1
                    else:
                        sum += self.data[tempa][2] * b.data[tempb][2]
                        tempa += 1
                        tempb += 1
                if (sum != 0):
                    result.insert(r, c, sum)
                while (bpos < b.len and b.data[bpos][0] == c):
                    bpos += 1

            while (apos < self.len and self.data[apos][0] == r):
                apos += 1

        result.print()

    def print(self):
        print("Dimension:", self.row, "x", self.col)
        print("Sparse Matrix: \nRow Column Value")

        for i in range(self.len):
            print(self.data[i][0], self.data[i][1], self.data[i][2])


a = sparse_matrix(4, 4)
b = sparse_matrix(4, 4)

a.insert(1, 2, 10)
a.insert(1, 4, 12)
a.insert(3, 3, 5)
a.insert(4, 1, 15)
a.insert(4, 2, 12)
b.insert(1, 3, 8)
b.insert(2, 4, 23)
b.insert(3, 3, 9)
b.insert(4, 1, 20)
b.insert(4, 2, 25)
a.scaleBy(2)

print("Addition: ")
a.add(b)
print("\nMultiplication: ")
a.multiply(b)
print("\nTranspose: ")
atranspose = a.transpose()
atranspose.print()


