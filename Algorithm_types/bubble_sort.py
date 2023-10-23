def bubble_sort(arr):
    size = len(arr)
    indicator = True

    while indicator:
        indicator = False
        for j in range(1, size):
            if arr[j - 1] > arr[j]:
                indicator = True
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    return arr

# Example usage:
arr = [5, 2, 9, 3, 8]
sorted_arr = bubble_sort(arr)
print(sorted_arr)