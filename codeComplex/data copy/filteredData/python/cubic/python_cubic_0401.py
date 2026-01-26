import io
import os
from collections import Counter, defaultdict, deque


def solve(N, M, K, right, down):
    if K % 2 == 1:
        return (("-1 " * N) + "\n") * M

    K //= 2

    inf = float("inf")
    R = N
    C = M

    for row in right:
        row.append(inf)
        row.append(inf)
        row.append(inf)
    right.append([inf] * (C + 2))
    right.append([inf] * (C + 2))
    for row in down:
        row.append(inf)
        row.append(inf)
    down.append([inf] * (C + 2))
    down.append([inf] * (C + 2))
    down.append([inf] * (C + 2))

    def right_(r, c):
        return right[r][c - 1]

    def down_(r, c):
        return down[r - 1][c]

    def left(r, c):
        return right[r][c]

    def up(r, c):
        return down[r][c]

    dist = [[inf for _ in range(C + 2)] for _ in range(R + 2)]
    for r in range(R):
        for c in range(C):
            dist[r][c] = 0
    for _ in range(K):
        nextDist = [[inf for _ in range(C + 2)] for _ in range(R + 2)]
        for r in range(R):
            for c in range(C):
                nextDist[r][c] = min(
                    dist[r][c - 1] + right_(r, c),
                    dist[r][c + 1] + left(r, c),
                    dist[r - 1][c] + down_(r, c),
                    dist[r + 1][c] + up(r, c),
                )
        dist = nextDist
    return "\n".join(" ".join(str(2 * dist[r][c]) for c in range(C)) for r in range(R))


def main(n):
    if n < 1:
        n = 1
    N = n
    M = n
    K = 2 * n
    right = []
    for i in range(N):
        row = []
        for j in range(M - 1):
            row.append((i + 1) * (j + 2))
        right.append(row)
    down = []
    for i in range(N - 1):
        row = []
        for j in range(M):
            row.append((i + 2) * (j + 1))
        down.append(row)
    ans = solve(N, M, K, right, down)
    # print(ans)
    pass
if __name__ == "__main__":
    main(3)