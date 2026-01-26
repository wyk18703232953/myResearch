n,l,r,x = map(int,input().split())
c = list(map(int,input().split()))
ans = 0

for mask in range(1 << n):
    a = []
    for bit in range(n):
        if mask & (1 << bit):
           a.append(c[bit])
    if len(a) >= 2 and max(a) - min(a) >= x and l <= sum(a) and sum(a) <= r:
        ans += 1
print(ans)        
