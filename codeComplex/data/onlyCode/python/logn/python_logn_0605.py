def binary(n,k,low,high):
    if low<=high:
        mid=(low+high)//2
        if (mid*(mid+1))//2-(n-mid)==k:
            return n-mid
        elif mid*(mid+1)//2-(n-mid)>k:
            return binary(n,k,low,mid-1)
        else:
            return binary(n,k,mid+1,high)

n,k=[int(x) for x in input().split()]
print(binary(n,k,1,n))