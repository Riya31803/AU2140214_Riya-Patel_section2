# Done inserting an element at the end

def insatid(arr,ele):
    arr=arr+[ele]
    return arr    
     
arr=[]




n=int(input("Enter no of elements: "))
arr=[0]* n
for i in range(n):
    arr[i]=int(input("enter: "))

  
print(arr)

ele=int(input("Enter element to be inserted: "))

print("Appended array is ",insatid(arr,ele))

