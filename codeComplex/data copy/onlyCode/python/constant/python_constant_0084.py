import math
n=int(input())
if(n==4): print(12)
elif(n<=2): print(n)
else:
    if(n%2==0):
        a=n*(n-1)*(n-3)
        if(n%3==0): a=a//3
        b=n*(n-1)*(n-2)
        b=b//2
        print(max(a,b,(n-1)*(n-2)*(n-3)))
    else: print(n*(n-1)*(n-2))