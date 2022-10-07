# Merge Sort

def mergeseq(arr,first,last,end,temp):
     a=first
     b=last
     m=0

     while(a<last and b<end):
        if arr[a]<arr[b]:
            temp[m]=arr[a]
            a=a+1
        else:
            temp[m]=arr[b]
            b=b+1
        m=m+1  
     while a<last:
        temp[m]=arr[a]
        a=a+1
        m=m+1
     while b<end:
        temp[m]=arr[b]
        b=b+1
        m=m+1
     for i in range(end-first):
        arr[i+first] = temp[i]   


def recMer(arr,f,l,temp):

    if f==l:
        return

    else:
        mid=(f+l)//2

    recMer(arr,f,mid,temp)
    recMer(arr, mid+1, l, temp)   

    mergeseq(arr, f, mid+1, l+1, temp)

def MergeSort(arr):

    n=len(arr)
    temp=[-1]*n
    recMer(arr, 0, n-1, temp)
    
    return temp

arr=[11,36,13,29,51,27]
print("Array",arr)
print("Sorted array",MergeSort(arr))





