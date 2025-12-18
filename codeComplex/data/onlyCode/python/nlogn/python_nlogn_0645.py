n, m = map(int, input().split())
y = []
for i in range(n):
    y.append(int(input()))
y.append(10 ** 9)
x = []
for i in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        x.append(b)
y.sort(); x.sort()
m = len(x)
ans = m
k = 0
for i in range(n + 1):
    ok = True
    for j in range(k, m):
        if y[i] <= x[j]:
            k = j
            ok = False
            break
    if ok:
        k = m
        ans = min(ans, m - k + i)
        break
    ans = min(ans, m - k + i)
print(ans)
#    
