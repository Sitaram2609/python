


x, n, m = map(int, input().split())  # Corrected input handling

for i in range(n, m-1 , -1):  # Fixing 'for' loop syntax and ensuring range is inclusive
    if i % x == 0:
        print(i,end=" ")
