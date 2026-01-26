def digit(a):
    s=0
    while a:
        s+=a%10
        a//=10
    return s

def big(n,s):
    lo=1
    hi=n
    while lo<=hi:
        mid=(lo+hi)//2
        if mid-digit(mid)<s:
            lo=mid+1
        else:
            hi=mid-1
    return n-lo+1

a,b=map(int,input().strip().split())
print(big(a,b))