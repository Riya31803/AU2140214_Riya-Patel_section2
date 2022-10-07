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


arr=[11,4,7,6,32,27] 
print(B_insertion_sort(arr))     