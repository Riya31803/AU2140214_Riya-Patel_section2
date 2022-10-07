# quick sort using random pivoting

import random
  
def Quicksort(arr, start , stop):
    if(start < stop):
          
       
        piv = partitionrand(arr,start, stop)
          
        Quicksort(arr , start , piv-1)
        Quicksort(arr, piv + 1, stop)
  
def partitionrand(arr , start, stop):
  
    randpivot = random.randrange(start, stop)

    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition(arr, start, stop)
  

def partition(arr,start,stop):
    pivot = start 
      
    i = start + 1 
      
    for j in range(start + 1, stop + 1):
      
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)
  


array = [10, 7, 8, 9, 1, 5]
Quicksort(array, 0, len(array) - 1)
print(array)
