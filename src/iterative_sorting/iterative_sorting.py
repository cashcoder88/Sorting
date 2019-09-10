# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    length = len(arr) - 1
    for i in range(0, length):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j]< arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[cur_index]        
   # TO-DO: swap

    return arr

def selection_sort2(arr):
    #divide the array into sorted and unosrted
    #loop through each element
    for i in range(0, len(arr)-1):
        current_index = i
        smallest_index = current_index

    #find the smallest element in the unsorted
        for j in range(current_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
    #put the smallest element at the end of the sorted 
        #swap the first element of unsorted with the smallest element
        arr[smallest_index], arr[current_index] = arr[current_index], arr[smallest_index]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    length = len(arr)-1
    for i in range(0, length):
        for j in range(0, length-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
#better implementation
def bubble_sort2(arr):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i]>arr[i+1]:
                #swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
array1 = [1, 5, 4, 8, 6, 9, 8, 5, 4, 3, 6]
print(bubble_sort(array1))
print(bubble_sort2(array1))
print(selection_sort(array1))
print(selection_sort2(array1))
# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr