def find_common_elements(s1, s2):
    # Convert strings to sets of characters
    set1 = set(s1)
    set2 = set(s2)
    
    # Find the common elements using intersection
    common_elements = set1.intersection(set2)
    
    # Convert the set of common elements back to a string
    result = ''.join(common_elements)
    
    return result

# Example usage
s1 = "sita"
s2 = "ram"
common_elements = find_common_elements(s1, s2)
print("Common elements:", common_elements)
