# Done replace an element in array

def replatind(a,pos,el,n):
    b=[]
    c=[]
    for i in range (n):
        if(i<pos-1):
            b=b+[a[i]]
        else:
            if(i>pos-1):
             b=b+[a[i]]        

    
     
    for j in range(n):
        if(j==pos-1):
            c=c+[el]
            
        else:
            if(j< pos-1):
                
                c=c+[b[j]]
            if(j> pos-1):
                c=c+[b[j-1]]
    print(c)
    
b=[]
c=[]
n=int(input("Enter no of elements: "))
a=[0]* n
for i in range(n):
    a[i]=int(input("enter: "))

pos=int(input("Enter the position:"))
el=int(input("Enter the new element:"))
replatind(a,pos,el,n)    


