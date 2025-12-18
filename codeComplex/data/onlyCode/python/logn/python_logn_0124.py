f = lambda m, k: (k*m - m*(m-1)//2 - m + 1)

def ok(m, k, n):
    return f(m, k) >= n

n, k = map(int, input().split())

if not ok(k, k, n): print(-1)
else: 
    l, h = 0, k
    while (h > l):
        mid = l + (h - l) // 2
        if ok(mid, k, n): h = mid
        else: l = mid + 1
    print(h)