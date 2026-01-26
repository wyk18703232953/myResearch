n, m = map(int, input().split())
b = list(map(int, input().split()))
g = list(map(int, input().split()))
mab = max(b)
mig = min(g)
if mab > mig:
    print(-1)
    exit()

b = sorted(b, reverse=True)
g = sorted(g)
num = 0
j = 0
for i in range(n):
    k = 0
    l = 1
    while j < m and k < m - l and b[i] <= g[j]:
        if b[i] == g[j]:
            l = 0
        num += g[j]
        j += 1
        k += 1
    num += b[i] * (m - k)

print(num)