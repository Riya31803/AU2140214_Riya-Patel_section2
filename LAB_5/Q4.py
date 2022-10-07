# insertion sort :  lINEAR  BINARY  AND  Selection Sort

import time
best1 = [i for i in range(1,10001)]
worst1 = [i for i in range(10001,0,-1)]
best2 = best1
worst2 = worst1


def binary(arr, num, l, f):
    if l == f:
        if arr[l] > num:
            return l
        else:
            return l + 1
    if l > f:
        return l
    mid = (l + f) // 2

    if (arr[mid] < num):
        return binary(arr, num, mid + 1, f)

    elif arr[mid] > num:
        return binary(arr, num, l, mid - 1)
    else:
        return mid


def B_insertion_sort(arr):
    for i in range(1, len(arr)):
        num = arr[i]
        k = binary(arr, num, 0, i - 1)
        arr = arr[:k] + [num] + arr[k:i] + arr[i + 1:]
    return arr

def L_insertionsort(arr):
    n=len(arr)

    for i in range (1,n):

        num = arr[i]
        pos = i

        while pos > 0 and num < arr[pos-1]:
           
            arr[pos] = arr[pos-1]
            pos=pos-1

        arr[pos]= num
    return arr


   

def selectionsort(arr):

    
    n = len(arr)
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
    

print("*************For Selection sort****************:")
print("Best Sorted array:")
b = time.time()
x=selectionsort(best2)
t = time.time()
print(t-b)

print("Worst Sorted array:")
b = time.time()
x=selectionsort(worst2)
t = time.time()
print(t-b)

print("**************For Binary Insertion sort******************:")
print("Best Sorted array:")
b = time.time()
x=B_insertion_sort(best1)
t = time.time()
print(t-b)

print("Worst Sorted array:")
b = time.time()
x=B_insertion_sort(worst1)
t = time.time()
print(t-b)

print("*****************For linear insertion sort*****************:")
print("Best Sorted array:")
b = time.time()
x=L_insertionsort(best1)
t = time.time()
print(t-b)

print("Worst Sorted array:")
b = time.time()
x=L_insertionsort(worst1)
t = time.time()
print(t-b)