# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # must compare 1st element of each
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # set index of both arrays to 0
    index_arr_a = 0
    index_arr_b = 0
    # loop through len of array range and put merged arr in
    for i in range(len(merged_arr)):
        # done with arr a default to b?
        if index_arr_a >= len(arrA):
            merged_arr[i] = arrB[index_arr_b]
            index_arr_b += 1
        # done with adding all of array b then default to array a
        elif index_arr_b >= len(arrB):
            merged_arr[i] = arrA[index_arr_a]
            index_arr_a += 1
        # smallest to the merged array
        elif arrA[index_arr_a] <= arrB[index_arr_b]:
            merged_arr[i] = arrA[index_arr_a]
            index_arr_a += 1 # iterate the pointer for the smaller value
        else:
            merged_arr[i] = arrB[index_arr_b]
            index_arr_b += 1
    return merged_arr

def merge_sort(arr):
    # check for 1
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2 # find midpoint
        # further divides left and right divide and conquer
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        # after merge to one array
        arr = merge(left, right)
        return arr
# test
arr = [1,3,2,4,6,2,7,9,8] 
arr = merge_sort(arr)
print(arr)

# TO-DO: implement the Merge Sort function below recursively


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

