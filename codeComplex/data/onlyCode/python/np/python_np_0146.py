n, m = map(int, input().split())
a = [0 for i in range(n)]
l, r = 0, n - 1
m -= 1

for i in range(1, n + 1):
    cur = 2**(n - i - 1)

    if (m >= cur):
        m -= cur
        a[r] = i
        r -= 1
    else:
        a[l] = i
        l += 1
        
print(*a)
