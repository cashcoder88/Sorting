# TO-DO: complete the helpe function below to merge 2 sorted arrays
# we need to sort arrA and arrB
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # Start merging my single lists of one element together into large, sorted sets
    # Repeat 3 till the entire data set is reassembled
    b = 0 #current arrA index
    a = 0 #current arrB index
# for each index in the merged arr: elements
    for i in range(num_elements):
        # find the smallest first-item between arrA and arrB
        #add that to elements at its given index
        # increment the a/b counter to move through indexes
        if a >= len(arrA):
            #first case, A is empty, b in not
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrA):
            #second case, A is not empty, b is
            merged_arr[i] = arra[a]
            a += 1
        elif arrA[a] < arrB[b]:
            #third case, A has the smaller element
            merged_arr[i] = arrA[a]
            a += 1
        else:
            #fourth case, B has the smaller element
            merged_arr[i] = arrB[b]
            b += 1
    # return this new array
    return merged_arr
array1 = [1, 4, 3, 76, 32, 3, 11, 9, 12, 18, 5, 6]
print()
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # while more than one item in array passed in, we need to split in half!
    # once we are down to just one element, its officially sorted
    # a single element can not be out of order, its just one element
    if len(arr) > 1:
        # implementing the split
        halfway = len(arr) // 2
        # cutting in half
        left_array = arr[ : halfway]
        right_array = arr[halfway :]
        #sort each of the split arrays, recursion
        sorted_left = merge_sort(left_array)
        sorted_right = merge_sort(right_array)
        #this will keep going until length is 1
        #now lets merge the now sorted arrays 
        arr = merge(sorted_left, sorted_right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
