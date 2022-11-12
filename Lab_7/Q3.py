# Heap Sort

def heapify(arr, n, i):
	s = i 
	l = 2 * i + 1 
	r = 2 * i + 2 

	if l < n and arr[l] < arr[s]:
		s = l

	if r < n and arr[r] < arr[s]:
		s = r

	if s != i:
		(arr[i],
		arr[s]) = (arr[s],
						arr[i])

		heapify(arr, n, s)


def heapSort(arr, n):
	
	for i in range(int(n / 2) - 1, -1, -1):
		heapify(arr, n, i)

	
	for i in range(n-1, -1, -1):
		
		
		arr[0], arr[i] = arr[i], arr[0]

		
		heapify(arr, i, 0)


def Sorting(arr, n):
	
	for i in range(n):
		print(arr[i], end = " ")
	print()

if __name__ == '__main__':
	arr = [5, 7, 4, 3, 10]
	n = len(arr)

	heapSort(arr, n)

	print("**** Sorted array ****")
	Sorting(arr, n)

