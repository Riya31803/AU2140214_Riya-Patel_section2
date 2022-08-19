def prodarray(a,n,product):
    if(n<0):
        return product
    else:
        product=product*a[n]
        return prodarray(a,n-1,product)

a=[]
n=int(input("Number of elements in array: "))
for i in range(0,n):
   l=int(input("enter a number: "))
   a.append(l)

print("product is:",prodarray(a,n-1,1))  