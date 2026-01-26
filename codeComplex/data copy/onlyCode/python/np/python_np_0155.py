n,l,r,x = map(int,input().split())
c = [int(i) for i in input().split()]
ans = 0
for bit in range(2,1<<n):
    probs = []
    t = 0
    for i in range(n):
        if bit&(1<<i):
            probs.append(c[i])
            t += c[i]
    
    a = min(probs)
    b = max(probs)

    if t >= l and t <= r and abs(a-b) >= x:
        ans += 1
print(ans)