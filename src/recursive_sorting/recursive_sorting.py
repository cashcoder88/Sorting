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


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

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
