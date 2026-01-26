n, k = map(int, input().split())

if n == 1:
    print(0)
elif k + (k - 1) * (k - 2) // 2 < n:
    print(-1)
else:
    l = 0
    r = k - 1  
    while r - l > 1:
        m = (l + r) // 2
        if  (2*k - m + 1) * m // 2 - (m - 1) >= n:
            r = m
        else: 
            l = m
    print(r)

