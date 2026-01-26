def search(arr,power):
    lo=0
    hi=len(arr)-1
    ans=-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]<=power:
            ans=mid
            lo=mid+1
        else:
            hi=mid-1
    return ans

n,q = list(map(int, input().split()))
a = list(map(int, input().split()))
k = list(map(int, input().split()))
for i in range(1,n):
    a[i]+=a[i-1]
power = 0
for i in range(q):
    power+=k[i]
    pos = search(a,power)
    if pos==n-1:
        print(n)
        power=0
    elif pos==-1:
        print(n)
    else:
        print(n-pos-1)