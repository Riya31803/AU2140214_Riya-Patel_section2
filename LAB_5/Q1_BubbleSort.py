# Bubble sort

arr=[11,4,7,6,32,27]
n=len(arr)


for i in range (n-1):

    for j in range (n-i-1):
        if(arr[j]>arr[j+1]):

            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
            print(arr)
        
print("\nSorted array",arr)   
   
        


