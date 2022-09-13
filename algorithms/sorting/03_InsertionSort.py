arr = [6 ,1 ,2 ,5, 4, 7,3 ,9 , 8 ]
print(arr)

#Notes:
# 1. Similar to Selection sort , given array is divided into 2 logical part ->sorted and non sorted
# 2. Initially sorted array hold arr[0]. Size of sorted array is 1
#    Size of non sorted array is len(arr)-1
# 3. In each subsequent iteration sorted array size increase by 1 and non sorted array size decrease by one

# 4. Outer for loop iterates from 1 to len(arr)
# 5. i act as boundary for sorted and non sorted array
# 6. arr[i] is the newest element which is going to be added in sorted array
# 7. Inner for loop operated on sorted array. Identify the position of sorted array and insert it.

def insertion_sort_inc(arr):
    for i in range(0, len(arr)):
        element = arr[i]  #current element
        sortedIndex= i-1  #rep the last index till it is sorted

        # if element > arr[sortedIndex]:
        #    move next iteration on outer loop,( inserting element to right)
        # else
        #    while loop
        #        swap element to required position (inserting element to left)
        if element > arr[sortedIndex]:
            #do nothing
            continue
        else:
            index = i-1
            #loop from i-1 till zeroto figure out position of new insert
            while index >= 0 and element < arr[index]:
                arr[index] , arr[index+1]= arr[index+1], arr[index]
                index= index -1

    print('Insertion ->' + str(arr))
    return None

insertion_sort_inc(arr)
