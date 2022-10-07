# Quick sort with pivot at middle

def part(arr, low, high):

	pivot = arr[high]

	i = low - 1

	for j in range(low, high):
		if arr[j] <= pivot:
			
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]

	(arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

	return i + 1

def QuickSort(arr, low, high):
    
	if low < high:

		x = part(arr, low, high)

		QuickSort(arr, low, x - 1)
		QuickSort(arr, x + 1, high)
        
arr = [11,3,17,8,23,9,5,10]
QuickSort(arr, 0, len(arr) - 1)
print(f'Sorted array: {arr}')
