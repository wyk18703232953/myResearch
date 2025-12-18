n, a, b, c, t = map(int, input().split())
l = list(map(int, input().split()))
f = [0] * 1001
for i in l: f[i] -= -1
tmp = 0
tmp2 = 0
for i in range(1, t):
    tmp += (t - i) * f[i]
tmp = n * a + tmp * c - tmp * b
print(max(n * a, tmp))