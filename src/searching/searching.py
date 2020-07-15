# TO-DO: Implement a recursive implementation of binary search
def binary_search_recursive(data, target, start, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_search_recursive(data, target, low, mid-1)
		else:
			return binary_search_recursive(data, target, mid+1, high)


data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,378]
target = 378

print(binary_search_recursive(data, target, 0, len(data)-1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
# base case
# recursion case (how to get to base case)
# can be solved with iteration


def sum_min(arr):
    if len(arr) == 1:
        return min(arr[0])
    else:
        return min(arr[0]) + sum_min(arr[1:])