def rotate_right(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > len(arr)
    
    for _ in range(k):
        last = arr[-1]  # Store last element
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]  # Shift elements right
        arr[0] = last  # Place last element at the beginning

# Example
arr = [1, 2, 3, 4, 5]
k = 2
rotate_right(arr, k)
print(arr)  # Output: [4, 5, 1, 2, 3]

def rotate_left(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > len(arr)
    
    for _ in range(k):
        first = arr[0]  # Store first element
        for i in range(n-1):
            arr[i] = arr[i+1]  # Shift elements left
        arr[-1] = first  # Place first element at the end

# Example
arr = [1, 2, 3, 4, 5]
k = 2
rotate_left(arr, k)
print(arr)  # Output: [3, 4, 5, 1, 2]