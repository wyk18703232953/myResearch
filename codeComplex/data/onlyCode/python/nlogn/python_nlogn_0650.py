n, m = map(int, input().split())
V = []
for i in range(n):
    V.append(int(input()))
V.sort()
V.append(10 ** 9)
n += 1
X2 = []
for i in range(m):
    x1, x2, y = map(int, input().split())
    if x1 == 1:
        X2.append(x2)
X2.sort()
k = len(X2)
i = 0
j = 0
ans = 10 ** 9 + 7
c = 0

while i < n:
    while j < k:
        if X2[j] < V[i]:
            c += 1
            j += 1
        else:
            break
    ans = min(ans,  k - c + i)
    i += 1
print(ans)