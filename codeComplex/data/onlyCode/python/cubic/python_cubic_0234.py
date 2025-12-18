import io
import os

from collections import Counter, defaultdict, deque


def solveBFS(NR, NG, NB, R, G, B):
    def pack(i, j, k):
        return i * 256 * 256 + j * 256 + k

    def unpack(ijk):
        i, jk = divmod(ijk, 256 * 256)
        j, k = divmod(jk, 256)
        return i, j, k

    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)
    dp = [0 for i in range(256 ** 3)]
    q = deque([0])
    while q:
        ijk = q.popleft()
        d = dp[ijk]
        i, j, k = unpack(ijk)

        if i < NR:
            r = R[i]

        if j < NG:
            g = G[j]
        if k < NB:
            b = B[k]
        if i + 1 <= NR and j + 1 <= NG:
            rg = pack(i + 1, j + 1, k)
            dp[rg] = max(dp[rg], r * g + d)
            q.append(rg)

        if i + 1 <= NR and k + 1 <= NB:
            rb = pack(i + 1, j, k + 1)
            dp[rb] = max(dp[rb], r * b + d)
            q.append(rb)

        if j + 1 <= NG and k + 1 <= NB:
            gb = pack(i, j + 1, k + 1)
            dp[gb] = max(dp[gb], g * b + d)
            q.append(gb)

    return max(dp)


def solve(NR, NG, NB, R, G, B):
    assert NR == len(R)
    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)

    R += [0]
    G += [0]
    B += [0]

    NR1 = NR + 2
    NG1 = NG + 2
    NB1 = NB + 2
    dp = [0 for i in range((NR1) * (NG1) * (NB1))]

    def pack(i, j, k):
        return i * NG1 * NB1 + j * NB1 + k

    inf = float("inf")
    for i in range(NR + 1):
        for j in range(NG + 1):
            dp[pack(i, j, -1)] = -inf
    for i in range(NR + 1):
        for k in range(NB + 1):
            dp[pack(i, -1, k)] = -inf

    for j in range(NG + 1):
        for k in range(NB + 1):
            dp[pack(-1, j, k)] = -inf

    for l in range(2, NR + NG + NB + 1, 2):
        for j in range(NG + 1):
            for k in range(NB + 1):
                i = l - j - k
                if i < 0 or i > NR:
                    continue
                r = R[i - 1]
                g = G[j - 1]
                b = B[k - 1]
                dp[pack(i, j, k)] = max(
                    r * g + dp[pack(i - 1, j - 1, k)],
                    r * b + dp[pack(i - 1, j, k - 1)],
                    b * g + dp[pack(i, j - 1, k - 1)],
                )

    return max(dp)


if False:
    import random

    random.seed()
    N = 5
    for t in range(100):
        R = [random.randint(1, 10) for i in range(random.randint(1, N))]
        G = [random.randint(1, 10) for i in range(random.randint(1, N))]
        B = [random.randint(1, 10) for i in range(random.randint(1, N))]
        ans1 = solveBFS(len(R), len(G), len(B), R, G, B)
        ans2 = solve(len(R), len(G), len(B), R, G, B)
        if ans1 != ans2:
            print(ans1, ans2)
            print(R, G, B)
        exit()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    NR, NG, NB = [int(x) for x in input().split()]
    R = [int(x) for x in input().split()]
    G = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans = solve(NR, NG, NB, R, G, B)
    print(ans)

