# Riya Patel  AU2140214

# 2 D array hashing number

class HashTable:
    def __init__(self):

        self.col = 5
        self.row = 5

        self.arr = [[None] for i in range(5)]

    def add(self):
        
        for i in keys:
          
            pos1 = i % self.row
            j=len(self.arr[pos1])
            self.arr[pos1][j-1]=i
            print(self.arr)
       

keys=[11,2,4,6,5]

Ht=HashTable()
Ht.add()
      