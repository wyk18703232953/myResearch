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

    dist = [[inf for i in range(C + 2)] for j in range(R + 2)]
    for r in range(R):
        for c in range(C):
            dist[r][c] = 0
    for k in range(K):
        nextDist = [[inf for i in range(C + 2)] for j in range(R + 2)]
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


DEBUG = False
if DEBUG:
    import random

    random.seed(0)
    for _ in range(1):
        N = 500
        M = 500
        K = 20

        def pack(i, j):
            return i * M + j

        def unpack(ij):
            return divmod(ij, M)

        graph = [[] for i in range(N * M)]

        right = [[random.randint(1, 10 ** 6) for j in range(M - 1)] for i in range(N)]
        down = [[random.randint(1, 10 ** 6) for j in range(M)] for i in range(N - 1)]
        print("tc" + str(_))
        ans = solve(N, M, K, right, down)
        # print(ans, ans1)
        # assert ans == ans1

    exit()


if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    def pack(i, j):
        return i * M + j

    def unpack(ij):
        return divmod(ij, M)

    N, M, K = [int(x) for x in input().split()]

    right = [[int(x) for x in input().split()] for i in range(N)]
    down = [[int(x) for x in input().split()] for i in range(N - 1)]

    ans = solve(N, M, K, right, down)
    print(ans)
