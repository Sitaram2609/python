def max_occurrence(arr):
    # Create a dictionary to store the count of each element
    count_dict = {}
    
    # Count occurrences of each element in the list
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Find the element with the maximum occurrence
    max_occurrence = max(count_dict.values())
    max_element = None
    for key, value in count_dict.items():
        if value == max_occurrence:
            max_element = key
            break
    
    return max_element

# Example usage
input_list = [1, 1, 2, 2, 2, 3, 3]
result = max_occurrence(input_list)
print("Element with maximum occurrence:", result)
