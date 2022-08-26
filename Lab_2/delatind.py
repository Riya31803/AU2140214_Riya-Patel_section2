# done delete an element from given position from array

def delatind(a,pos,n):

    b=[]
    for i in range (n):
        if(i<pos-1):
            b=b+[a[i]]
        else:
            if(i>pos-1):
             b=b+[a[i]]        

    
    print(b)
    
    
    

b=[]
n=int(input("Enter no of elements: "))
a=[0]* n
for i in range(n):
    a[i]=int(input("enter: "))

  
print(a)
pos=int(input("Enter the position of element to be deleted: "))

delatind(a,pos,n)