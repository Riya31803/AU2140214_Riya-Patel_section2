# Riya Patel  AU2140214
#  Quadrating probing

class HashTable:
    def __init__(self):

        self.M1 = 17
        self.M2 = 37
        
        self.hash1=[None for i in range (17)]
        self.hash2=[None for i in range (37)] 

    def add(self):

        for i in keys:
            pos1 = i % self.M1
            pos2 = i % self.M2
            j=0
            if self.hash1[pos1]==None:
                self.hash1[pos1]=i
            else:
                temp1=pos1
                while (self.hash1[temp1]!=None  and temp1<self.M1):
                    temp1=(pos1+ (j*j)) % self.M1
                    j=j+1
                self.hash1[temp1]=i

            if self.hash2[pos2]==None:
                self.hash2[pos2]=i
            else:
                temp2=pos2
                while (self.hash2[temp2]!=None and temp2<self.M2):
                    temp2=(pos2+ (j*j)) % self.M2
                    j=j+1
                self.hash2[temp2]=i            
            
        print(self.hash1)
        print(self.hash2)
    
    def check(self,num):
        for i in range (3):
            if num[i] in self.hash1:
                print(num[i]," is in hash 1")
            if num[i] in self.hash2:
                print(num[i]," is in hash 2")
            if num[i] not in self.hash1:
                print(num[i]," is not in hash 1")

            if num[i] not in self.hash2:
                print(num[i]," is not in hash 2")    


num=[100,133,174]
keys=[133,84,92,221,174]


Ht=HashTable()
Ht.add()
print("\n")
Ht.check(num)