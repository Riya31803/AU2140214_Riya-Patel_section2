# Done searching an element from the array

def srch(a,element):

    for j in range(n-1):
        if(a[j]==element):
            z= j+1
        else:
            z=-1
    return z
    

n=int(input("Enter no of elements: "))
a=[0]* n
for i in range(n):
    a[i]=int(input("enter: "))

  
print(a)

element=int(input("Enter element to be searched: "))


print("Index of ",element,"is",srch(a,element))   