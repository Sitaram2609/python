n=5


for i in range(1,n+1):
    for j in range (1,i+1):
        print(j,end=' ')
    print()

print()

# First pattern (descending)
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print()

for i in range(n, 0, -1):  # Loop from 5 to 1
    print("  " * (n - i), end="")  # Print leading spaces
    for j in range(1, i + 1):  # Print numbers from 1 to i
        print(j, end=" ")
    print() 