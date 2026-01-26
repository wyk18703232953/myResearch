from sys import stdin
input = stdin.readline

n = int(input())
a = []
for i in range(4):
    a.append([[int(x) for x in list(input().rstrip())] for _ in range(n)])
    if i < 3: input()
b = []
for i in range(4):
    b.append([])
    for j in range(2):
        c = 0
        for y in range(n):
            for x in range(n):
                if j == 1:   
                    z = (x + y) % 2
                else:
                    z = 1 - (x + y) % 2
                c += a[i][y][x] != z
        b[-1].append(c)
ans = float("inf")
for i in (3, 5, 6, 9, 10, 12):
    ans = min(ans, b[0][i & 1] + b[1][i >> 1 & 1] + b[2][i >> 2 & 1] + b[3][i >> 3 & 1])
print(ans)