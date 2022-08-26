# Done inserting an element at a given position

def insatind(a,pos,el,n):
    b=[]
    for i in range(0,n+1):
        if(i==pos-1):
            b=b+[el]
            
        else:
            if(i< pos-1):
                
                b=b+[a[i]]
            if(i> pos-1):
                b=b+[a[i-1]]
    print(b)

b=[]
n=int(input("Enter no of elements: "))
a=[0]* n
for i in range(n):
    a[i]=int(input("enter: "))
pos=int(input("Enter the position:"))
el=int(input("Enter the element:"))
insatind(a,pos,el,n)

