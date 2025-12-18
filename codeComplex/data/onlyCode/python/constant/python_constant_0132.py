def resistors(a,b):
    ans=0
    while b:
        ans+=a//b
        a,b=b,a%b
    return ans
a,b=map(int,input().strip().split())
print(resistors(a,b))