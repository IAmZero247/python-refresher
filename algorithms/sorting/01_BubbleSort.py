
arr = [6 ,1 ,2 ,5, 4, 7,3 ,9 , 8 ]
print(arr)

#Notes:
# 1. Outer loop need to iterate till second last element
# 2. Inner loop need to iterate till length-i-1
# 3. Inside the inner loop swap j and j+1 element based on inc or dec sorting
def bubble_sort_inc(arr):
    for i in range(0, len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                 arr[j] ,arr[j+1] = arr[j+1], arr[j]
    print('Bubble ->' + str(arr))
    return None

bubble_sort_inc(arr)
