# Done inserting an element  in the beginning

def insatbeg(a,el,n):
    b=[]
    for i in range(0,n+1):
        if(i==0):
            b=b+[el]
        else:
            b=b+[a[i-1]]
    print("appended array is ",b)

b=[]
n=int(input("Enter no of elements: "))
a=[0]* n
for i in range(n):
    a[i]=int(input("enter: "))

  

print("Original array is : ",a)

el=int(input("Enter the element to be inserted: "))
insatbeg(a, el, n)