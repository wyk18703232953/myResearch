def binarySearch (N,l,r,x): 
    if r >= l: 
        mid = l + (r - l)//2
        Temp = (mid*(mid+1))//2
        if Temp-x == N-mid: 
            return N-mid 
        elif Temp-x > N-mid: 
            return binarySearch(N,l, mid-1, x)  
        else: 
            return binarySearch(N,mid + 1, r, x) 
    else: 
        return -1
n,k=list(map(int,input().split()))
print(binarySearch (n,0,n,k))