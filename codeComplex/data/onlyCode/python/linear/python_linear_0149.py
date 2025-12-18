n, p = map(int, input().split())
a = list(map(int, input().split()))
t = 0
k = 0
for i in range(n):
    k += a[i]
s = 0
for i in range(0, n-1):
    s += a[i]
    t = max(t, s%p + (k - s)%p)
print(t)
