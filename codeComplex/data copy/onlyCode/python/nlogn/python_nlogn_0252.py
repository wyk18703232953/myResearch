
def bin_ser(arr,curr):
    l=0
    r=len(arr)-1
    ans=-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]<=curr:
            ans=mid
            l=mid+1
        else:
            r=mid-1
    return ans


def main():
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    su=sum(arr)
    curr=0
    for i in range(1,n):
        arr[i]=arr[i]+arr[i-1]
    for b in brr:
        curr+=b
        pos=n-bin_ser(arr,curr)-1
        if pos==0:
            pos=n
        print(pos)
        if curr>=su:
            curr=0

main()