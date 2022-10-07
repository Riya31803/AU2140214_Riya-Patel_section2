# Radix Sort

def Max(arr):
    n=len(arr)
    max=arr[0]
    for i in range(n):
        if arr[i]>max:
            max=arr[i]
    return max


def countingSort(arr, exp1):

	n = len(arr)
	out = [0] * (n)

	count = [0] * (10)

	for i in range(0, n):
		pos = (arr[i]/exp1)
		count[int((pos)%10)] += 1

	for i in range(1,10):
		count[i] += count[i-1]

	i = n-1
	while i>=0:
		pos = (arr[i]/exp1)
		out[ count[ int((pos)%10) ] - 1] = arr[i]
		count[int((pos)%10)] -= 1
		i -= 1

	i = 0
	for i in range(0,n):
		arr[i] = out[i]

def radixSort(arr):

	max1 = Max(arr)

	exp = 1
	while max1/exp > 0:
		countingSort(arr,exp)
		exp *= 10

arr = [ 11,43,76,25,64,120,111,1]
radixSort(arr)
n = len(arr)
print("Sorted array")
for i in range(n):
	print(arr[i],end=" ")



