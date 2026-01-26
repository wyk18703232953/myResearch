n,l,r,x = map(int,input().split())
A = list(map(int,input().split()))
count = 0
for i in range(1<<n):
    total = 0
    mn = 1e6
    mx = -1e6
    for k in range(n):
        if (i & (1<<k)):
            total += A[k]
            mn = min(A[k],mn)
            mx = max(A[k],mx)
    if total<=r and total>=l and mx-mn>=x:
        count += 1
print(count)