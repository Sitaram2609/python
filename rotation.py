original_arr = [2, 3, 4, 5]
rotated_arr = [3, 4, 5, 2]

# Find the index of the last element of the original array in the rotated array
right_rotations = rotated_arr.index(original_arr[0])

print("Right rotations needed:", right_rotations)  



original_arr = [2, 3, 4, 5]
rotated_arr = [3, 4, 5, 2]

# Find the index of the first element of the original array in the rotated array
left_rotations = len(rotated_arr) - rotated_arr.index(original_arr[0])

print("Left rotations needed:", left_rotations)
