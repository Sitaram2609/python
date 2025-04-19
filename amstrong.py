n=153

org=n

res=0
while n!=0:

    rem=n % 10
    res=res+ rem**3
    n//=10


print(res==org)