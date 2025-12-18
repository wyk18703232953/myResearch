import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [list(input().rstrip()) for _ in range(n)]
t = [[1000] * m for _ in range(n)]
ok1 = [[0] * m for _ in range(n)]
ok2 = [[0] * m for _ in range(n)]
for i in range(n):
    si = s[i]
    c = 0
    for j in range(m):
        if si[j] == "*":
            c += 1
        else:
            c = 0
        t[i][j] = min(t[i][j], c)
    c = 0
    for j in range(m - 1, -1, -1):
        if si[j] == "*":
            c += 1
        else:
            c = 0
        t[i][j] = min(t[i][j], c)
for j in range(m):
    c = 0
    for i in range(n):
        if s[i][j] == "*":
            c += 1
        else:
            c = 0
        t[i][j] = min(t[i][j], c)
    c = 0
    for i in range(n - 1, -1, -1):
        if s[i][j] == "*":
            c += 1
        else:
            c = 0
        t[i][j] = min(t[i][j], c)
ans = []
for i in range(n):
    for j in range(m):
        tij = t[i][j] - 1
        if tij >= 1:
            ans.append((i + 1, j + 1, tij))
            ok1[max(0, i - tij)][j] += 1
            if i + tij + 1 < n:
                ok1[i + tij + 1][j] -= 1
            ok2[i][max(0, j - tij)] += 1
            if j + tij + 1 < m:
                ok2[i][j + tij + 1] -= 1
for i in range(1, n):
    for j in range(1, m):
        ok1[i][j] += ok1[i - 1][j]
        ok2[i][j] += ok2[i][j - 1]
for i in range(n):
    for j in range(m):
        if s[i][j] == "*":
            if not (ok1[i][j] or ok2[i][j]):
                ans = -1
                print(ans)
                exit()
k = len(ans)
print(k)
for ans0 in ans:
    print(*ans0)