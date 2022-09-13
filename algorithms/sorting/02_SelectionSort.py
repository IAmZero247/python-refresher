arr = [6 ,1 ,2 ,5, 4, 7,3 ,9 , 8 ]
print(arr)

#Notes:
# 1. Logically segment given arr into sorted array and non sorted array
#     arr -> sorted | non-sorted
# 2. Initially sorted array has zero elements
# 3. In each iteration sorted array size increase by 1 and non sorted array size decrease by one
# 4. Each iteration identify lowest element in non sorted array and put that value in sorted array


# 4. Outer for loop iterates from 0 to len(arr)
# 5. i act as boundary for sorted and non sorted array
# 6. i is consider as the element with lowest value
# 7. Inner for loop operated on non sorted array
def sorted_sort_inc(arr):
    for i in range(0, len(arr)):
        min_element_index = i
        # i act as boundary for sorted and non sorted array
        # sorted array -> 0 to i
        # non sorted array -> i+1 to len(arr)
        # second loop iterates on non sorted array , means from i+1
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_element_index]:
                 min_element_index = j
        if min_element_index is not i:
            arr[i], arr[min_element_index] = arr[min_element_index], arr[i]
    print('SelectionSort ->' + str(arr))
    return None

sorted_sort_inc(arr)
