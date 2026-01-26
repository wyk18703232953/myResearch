import math


n=int(input())

for _ in range(n):
    a,b=map(int,input().split())
    ans=0
    while a>0 and b>0:
        if a>=b:
            ans+=a//b
            a=a%b
        else:
            ans+=b//a
            b=b%a
    print(ans)
        