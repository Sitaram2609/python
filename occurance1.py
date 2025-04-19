def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)
    for i in range(len(string) - sub_len + 1):
        if string[i:i + sub_len] == sub_string:
            count += 1
    return count

# Fixing the if condition
if __name__ == '__main__':
    string = input("Enter the main string: ").strip()
    sub_string = input("Enter the substring to count: ").strip()

    count = count_substring(string, sub_string)
    print("Occurrences:", count)
