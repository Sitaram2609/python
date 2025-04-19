num=121
rev=0

reg=num

while num !=0:
    rem=num%10
    rev=rev*10+rem
    num//=10



if reg==rev:
    print("yes")

else:
    print("no")    



  