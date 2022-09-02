# Riya Patel  AU2140214

class Game_of_Life:

    def __init__(self,rows,cols):
        self.array=[0]*rows
        for i in range(rows):
            self.array[i]=[0]*cols

    def numrow(self):
        return len(self.array)

    def numcol(self):
        return len(self.array[0])

    def print2d(self):
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                print(self.array[i][j],end=" ")
            print("")

    def configure(self,coordList):
        # coordlist=[(r1,c1),(r2,c2)...]
        for r,c in coordList:
            self.array[r][c]=1
        self.print2d()

    def clearCell(self,row,col):
        if (row <= len(self.array) and col<= len(self.array[0])):
            self.array[row][col] = 0
        else:
            print("Enter valid row and column value")

    def setCell(self,row,col):
        if (row <= len(self.array) and col<= len(self.array[0])):
            self.array[row][col] = 1
        else:
            print("Enter valid row and column value")

    def isLiveCell(self,row,col):
        if (row <= len(self.array) and col<= len(self.array[0])):
            return self.array[row][col] == 1
        else:
            print("Enter valid row and column value")

    def numLiveNeighbors(self ,row, col):
        trav = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        count = 0
        for x,y in trav:
            if(0<=row+x<len(self.array) and 0<=col+y<len(self.array[0]) and self.array[row+x][col+y]==1):
                count=count+1
        return count

    def start(self,row,col):
        count = self.numLiveNeighbors(row,col)
        if(self.array[row][col]==1):
            if 2<=count<=3:
                return 1
            else:
                return 0
        else:
            if count == 3:
                return 1
            else:
                return 0

    def final_solution(self):
        c=0
        while c!=10:
            for i in range(len(self.array)):
                for j in range(len(self.array[0])):
                    self.array[i][j]=self.start(i,j)
            print("Final")
            self.print2d()
            c = c + 1

tmp = Game_of_Life(5,6)
tmp.configure([(0,0),(0,1),(2,2),(1,0),(4,4),(4,5),(3,5)])
tmp.final_solution()