def digit(a):
    s=0
    while a:
        s+=a%10
        a//=10
    return s

def big(n,s):
    # lst=[[i,i-digit(i)] for i in range(1,n+1)]
    lo=1
    hi=n
    while lo<=hi:
        mid=(lo+hi)//2
        if mid-digit(mid)<s:
            # print(digit(mid))
            lo=mid+1
        else:
            hi=mid-1
            # hi=mid-1
    return n-lo+1

a,b=map(int,input().strip().split())
print(big(a,b))