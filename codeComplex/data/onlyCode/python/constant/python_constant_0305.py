k,n,s,p=map(int,input().split())
c=(n//s) if n%s==0 else (n//s)+1
print((c*k)//p if (c*k)%p==0 else ((c*k)//p)+1)

