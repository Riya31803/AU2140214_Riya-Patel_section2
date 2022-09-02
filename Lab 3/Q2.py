# Riya patel  AU2140214

def displayMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

class Array2D:
    def __init__(self,nrows,ncols):
        self.nrows=nrows
        self.ncols = ncols
        self.sparray=[]
    def numrow(self):
        return self.nrows

    def numcol(self):
        return self.ncols

    def clear(self,value):

        b=[]
        for i in range(self.nrows):
            for j in range(self.ncols):
                b.append([i,j,value])
        self.sparray=b


    def getitems(self,i1,i2):
        for i in range(len(self.sparray)):
            for x,y,z in self.sparray:
                if(x==i1 and y==i2):
                    return z
        return 0

    def setitems(self,i1,i2,value):
        c=0
        for i in range(len(self.sparray)):
            if (self.sparray[i][0]==i1 and self.sparray[i][1]==i2 ):
                self.sparray[i][2]=value
                c=c+1
        if(c==0):
            self.sparray.append([i1,i2,value])

a = Array2D(4,3)

a.setitems(8,1,3)
a.setitems(1,3,2)
a.setitems(2,3,2)
a.setitems(1,6,3)
print(a.sparray)
print("element at position ",a.getitems(2,2))


def SparseMatrix(matrix):
     sparseMatrix = []
     for i in range(len(matrix)):
         for j in range(len(matrix[0])):
             if matrix[i][j] != 0:
                 temp = []
                 temp.append(i)
                 temp.append(j)
                 temp.append(matrix[i][j])
                 sparseMatrix.append(temp)
     print("\nSparse Matrix: ")
     displayMatrix(sparseMatrix)

normal = [[3,0,1,0],
                 [0,3,0,0],
                 [0,2,0,0]]
displayMatrix(normal)

SparseMatrix(normal)


