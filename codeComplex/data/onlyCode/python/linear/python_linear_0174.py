n, k = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))
p = [0] * (n + 1)
now = 0
for i in range(0, n):
    if (t[i] == 1):
        now += a[i]
    p[i + 1] = p[i]
    if (t[i] == 0):
        p[i + 1] += a[i]
s = 0
for i in range(n - k + 1):
    s = max(s, p[i + k] - p[i])
print(now + s)
    