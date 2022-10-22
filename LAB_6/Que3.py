# Riya Patel  AU2140214

# Double hashing

class HashTable:

    def __init__(self):

        self.M1 = 17
        self.hash1=[None for i in range (17)]

    def add(self):

        for i in keys:
            pos1 = i % self.M1
            j=0

            # Hp function with P=11
            x = 1 + (i % 11)

            if self.hash1[pos1]==None:
                self.hash1[pos1]=i
            else:
                temp1=pos1
                while (self.hash1[temp1]!=None  and temp1<self.M1):
                    temp1=(pos1+ (j* x))% self.M1
                    j=j+1
                self.hash1[temp1]=i

        print(self.hash1)
    
    def check(self,num):
        for i in range (3):
            if num[i] in self.hash1:
                print(num[i]," is in hash 1")
            
            if num[i] not in self.hash1:
                print(num[i]," is not in hash 1")
   


num=[100,133,174]
keys=[133,84,92,221,174]


Ht=HashTable()
Ht.add()
print("\n")
Ht.check(num)