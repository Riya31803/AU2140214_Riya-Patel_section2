# Riya patel  AU2140214
class Array_2D:
    def __init__(self,rows,cols):
        self.array=[None]*rows
        for i in range(rows):
            self.array[i]=[None]*cols
    def numrow(self):
        return len(self.array)
    def numcol(self):
        return len(self.array[0])
    def print2D(self):
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                print(self.array[i][j],end=" ")
            print("")
    def setitem(self,i1,i2,value):
        if (i1 <= len(self.array) and i2 <= len(self.array[0])):
            self.array[i1][i2] = value
        else:
            print("Enter valid row and column value")

    def getitem(self,i1,i2):
        if(i1<=len(self.array) and i2<=len(self.array[0])):
            return self.array[i1][i2]
        else:
            print("Enter valid row and column value")

    def clear(self,value):
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                self.array[i][j]=value


a = Array_2D(3,3)

for i in range(len(a.array)):
    for j in range(len(a.array[0])):
        v=int(input("Enter elements: "))
        a.setitem(i,j,v)
    print("")
a.print2D()



print("\nElement at given position is : ",a.getitem(1,1))
print("-------CLEAR-------\n",a.clear(2))
a.print2D()
