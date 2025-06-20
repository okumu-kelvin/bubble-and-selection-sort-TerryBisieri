def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
        n = len(unsorted_list)
        for i in range(n):
            # Track if any swap was made
            swapped = False
            for j in range(0, n - i - 1):
                if unsorted_list[j] > unsorted_list[j + 1]:
                    # Swap elements
                    unsorted_list[j], [j + 1] = unsorted_list[j + 1], unsorted_list[j]
                    swapped = True
            if not swapped:
                break
        return unsorted_list

My_list=[3, 2, 1, 9, 5, 7, 8, 6]
print("Unsorted List: ", My_list)
sorted_list=bubble_sort(My_list)
print("Sorted List: ",sorted_list)
