def reverse_string_with_stack(s):
    # Initialize a stack
    stack = []

    # Push alphabetic and numeric characters to the stack
    for char in s:
        if char.isalnum():
            stack.append(char)

    # Create a list to store the result
    result = []

    # Pop from the stack for alphanumeric characters, keep non-alphanumeric characters in place
    for char in s:
        if char.isalnum():
            result.append(stack.pop())
        else:
            result.append(char)

    # Join the result list into a string
    return ''.join(result)