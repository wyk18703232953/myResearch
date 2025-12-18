def binary(n,k):
    lower=1
    upper=n
    while(lower<upper):
        mid=(lower+upper)//2
        total=(mid*(mid+1))//2
        if n-mid==total-k:
            print(n-mid)
            break
        else:
            if n-mid>total-k:
                lower=mid+1
            else:
                upper=mid

n,k=map(int,input().split())
if n==1 and k==1:
    print(0)
else:    
    binary(n,k)
