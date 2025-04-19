def remove_adjacent_pairs(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:  
            stack.pop()  # Remove the last element if it matches
        else:
            stack.append(char)  # Otherwise, add to stack
    
    return ''.join(stack)

# Example usage
input_str = "geek"
output_str = remove_adjacent_pairs(input_str)
print(output_str)  # Output: "gk"
