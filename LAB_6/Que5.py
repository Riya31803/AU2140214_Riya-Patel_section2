# Riya Patel  AU2140214

# Polynomial hash for a string

class HashTable:
    def __init__(self):

        self.M1 = 17
        self.M2 = 37
        
        self.hash1=[None for i in range (17)]
        self.hash2=[None for i in range (37)] 

    def add(self):

        a=1
        Sum=0
        for j in range(6):
        
            x = keys[j]
            n=len(x)
            for k in range (n):

                s=ord(x[k])
                Sum=Sum + (s*(a**(n-1)))
                n=n-1
            print("polynomial value of ",keys[j]," = ",Sum)
            pos1 = Sum % 17
            pos2 = Sum % 37
            print("hash value of ",keys[j]," = ",pos1,pos2)
            print("\n")
            if self.hash1[pos1]==None:
                self.hash1[pos1]=keys[j]
            else:
                temp1=pos1
                while (self.hash1[temp1]!=None  and temp1<self.M1):
                    temp1=temp1+1
                self.hash1[temp1]=keys[j]
            

            if self.hash2[pos2]==None:
                self.hash2[pos2]=keys[j]
            else:
                temp2=pos2
                while (self.hash2[temp2]!=None  and temp2<self.M2):
                    temp2=temp2+1
                self.hash2[temp2]=keys[j]
            
        print(self.hash1)
        print("\n")
        print(self.hash2)

keys=[['f','i','s','t'],['s','i','f','t'],['s','h','i','f','t'],['f','a','s','t'],['f','a','s','t','e','r'],['s','h','a','f','t']]



Ht=HashTable()
Ht.add()

