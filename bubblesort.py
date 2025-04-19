def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # After each pass, the largest element is in its correct position, so we reduce the number of comparisons
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
arr = [5, 3, 8, 4, 2]
bubble_sort(arr)
print(arr)  # Output: [2, 3, 4, 5, 8]