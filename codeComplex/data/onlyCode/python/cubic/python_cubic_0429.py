# URDL
DR = [1,0,-1,0]
DC = [0,1,0,-1]

n, m, k = map(int, input().split())
w = [[[0] * m for _ in range(n)] for _ in range(4)]
for r in range(n):
    for c, e in enumerate(map(int, input().split())):
        w[1][r][c] = w[3][r][c + 1] = e
for r in range(n - 1):
    for c, e in enumerate(map(int, input().split())):
        w[0][r][c] = w[2][r + 1][c] = e


INF = 10 ** 9


def solve():
    global k
    global w
    if k % 2 == 1:
        return [[-1] * m] * n
    k //= 2
    best = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
    for steps in range(1, k + 1):
        for r in range(n):
            for c in range(m):
                best[steps][r][c] = INF
                for d in range(4):
                    r2, c2 = r + DR[d], c + DC[d]
                    if 0 <= r2 < n and 0 <= c2 < m:
                        best[steps][r][c] = min(best[steps][r][c], 2 * w[d][r][c] + best[steps - 1][r2][c2])
    return best[k]


res = solve()
for e in res:
    print(*e)