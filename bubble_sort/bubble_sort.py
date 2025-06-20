def bubble_sort(arr):
    # TODO: Implement bubble sort
        n = len(arr)
        for i in range(n):
            # Track if any swap was made
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    # Swap elements
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

My_list=[3, 2, 1, 9, 5, 7, 8, 6]
print("Unsorted List: ", My_list)
sorted_list=bubble_sort(My_list)
print("Sorted List: ",sorted_list)
