# selection sort

def selectionsort(arr):
    
    n = len(arr)
    print("unsorted array",arr)
    for i in range( n - 1 ):

            small = i

            for j in range( i + 1, n ):
                if arr[j] < arr[small] :
                    small = j

            if small != i :
                tmp = arr[i]
                arr[i] =arr[small]
                arr[small] = tmp

    return arr
    
arr=[11,4,7,6,32,27] 
print(selectionsort(arr))          

