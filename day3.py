a = 0
b = 1
n = 7
fib = []

for _ in range(n):
    fib.append(a)
    c=a+b
    a=b
    b=c

print(fib)

