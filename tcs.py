# Taking input from the user
user_input = input("Enter numbers separated by space: ")

# Convert the input string into a list
arr = user_input.split()

# Replace the number '3' with the word 'three'
arr = ["three" if num == "3" else num for num in arr]

# Join the list back into a string and print the output
output = " ".join(arr)
print(output)
  