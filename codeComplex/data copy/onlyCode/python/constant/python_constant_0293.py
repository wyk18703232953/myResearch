k,n,s,p = map(int,input().split())
print(int((int((n+s-1)/s)*k+p-1)/p))