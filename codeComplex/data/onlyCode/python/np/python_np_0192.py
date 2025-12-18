n, l, r, x = map(int, input().split())
c = list(map(int, input().split()))

ans = 0

for mask in range(2**n):
    cnt, csum = 0, 0
    mn, mx = 10**18, -(10**18)
    for i in range(n):
        if (mask & (1 << i) != 0):
            cnt += 1
            csum += c[i]
            mn = min(mn, c[i])
            mx = max(mx, c[i])
    if (cnt >= 2) and (csum >= l) and (csum <= r) and (mx - mn >= x):
        ans += 1
        
print(ans)
    