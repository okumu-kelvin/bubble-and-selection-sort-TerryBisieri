def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
       
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
       
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

My_arr=[3, 2, 1, 9, 5, 7, 4, 8, 6]
print("Unsorted array: ", My_arr)
Sorted_arr=selection_sort(My_arr)
print("Sorted array: ", Sorted_arr)
