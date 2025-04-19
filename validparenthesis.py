s = '{}[]{}'
stack = []

pairs = {
    '{': '}',
    '(': ')',
    '[': ']'
}

for brac in s:
    if brac in pairs:  # If it's an opening bracket
        stack.append(brac)
    elif len(stack) == 0 or brac != pairs[stack.pop()]:  # Check for unmatched closing bracket
        print(False)  # Replace return with print since this is not inside a function
        break
else:
    print(len(stack) == 0)  # If loop completes, check if stack is empty
