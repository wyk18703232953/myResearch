from sys import stdin

rstr = lambda: stdin.readline().strip()
rints = lambda: [int(x) for x in stdin.readline().split()]

n, m, k = rints()
a = [rstr() for _ in range(n)]
mem = [[float('inf') if i else 0 for _ in range(k + 1)] for i in range(n + 1)]

for i in range(n):
    ixs = []
    for j in range(m):
        if a[i][j] == '1':
            ixs.append(j)

    for j in range(k + 1):
        tem = 0
        if j < len(ixs):
            tem, c = float('inf'), 0
            for j1 in range(len(ixs) - j - 1, len(ixs)):
                tem = min(tem, ixs[j1] - ixs[c] + 1)
                c += 1

        for j1 in range(k + 1 - j):
            mem[i + 1][j1 + j] = min(mem[i + 1][j1 + j], mem[i][j1] + tem)

print(mem[n][k])
# print(mem)
