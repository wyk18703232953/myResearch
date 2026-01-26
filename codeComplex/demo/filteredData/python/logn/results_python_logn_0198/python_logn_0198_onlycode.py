def digitsum(n):
    init=0
    for item in str(n):
        init+=int(item)
    return init
n,s=map(int,input().split())
if n-digitsum(n)<s:
    print(0)
else:
    i=0
    j=n
    while i<j:
        mid=(i+j)//2
        if mid-digitsum(mid)<s:
            i=mid+1
        else:
            j=mid
    else:
        print(n-i+1)