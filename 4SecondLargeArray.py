#Python program to find second largest number in array
# Method 1

def findLargest(arr):
	secondLargest = 0
	largest = min(arr)

	for i in range(len(arr)):
		if arr[i] > largest:
			secondLargest = largest
			largest = arr[i]
		else:
			secondLargest = max(secondLargest, arr[i])

	# Returning second largest element
	return secondLargest


# Calling above method over this array set
print(findLargest([10, 20, 4, 45, 99]))


print("______________________________")

# Method 2
# python code to print second largest element in array

lst = [10, 20, 4, 45, 99]
maximum1 = max(lst)
maximum2 = max(lst, key=lambda x: min(lst)-1 if (x == maximum1) else x)
print(maximum2)
