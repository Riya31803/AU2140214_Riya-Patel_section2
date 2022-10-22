# Riya Patel  AU2140214

# HashTable as Array of bits

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

            if self.hash1[pos1]==None:
                self.hash1[pos1]="1"
            else:
                temp1=pos1
                while (self.hash1[temp1]!=None  and temp1<self.M1):
                    temp1=temp1+1
                self.hash1[temp1]="1"

            if self.hash2[pos2]==None:
                self.hash2[pos2]="1"
            else:
                temp2=pos2
                while (self.hash2[temp2]!=None and temp2<self.M2):
                    temp2=temp2+1
                self.hash2[temp2]="1"          
            
        print(self.hash1)
        print(self.hash2)
    
    def check(self,num):
        for i in range (3):
            z= num[i] % self.M1
            y= num[i] % self.M2

            if z=="1":
                print(num[i]," is in hash 1")
            if y=="1":
                print(num[i]," is in hash 2")
            if z!="1":
                print(num[i]," is not in hash 1")

            if y!="1":
                print(num[i]," is not in hash 2")    


num=[100,133,174]
keys=[133,84,92,221,174]


Ht=HashTable()
Ht.add()
print("\n")
Ht.check(num)