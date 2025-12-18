n,k=map(int,input().split())
if n>=k:
    print((k-1)//2)
elif n*2>k:
    print(n-k//2)
else: print(0)
