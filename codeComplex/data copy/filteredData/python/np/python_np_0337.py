import sys

def main(n):
    # Map n to problem sizes
    N = max(1, n)
    M = max(1, (n + 1) // 2)

    # Deterministically generate table of size N x M
    # table[i][k] = (i * 131 + k * 17 + i * i + k * k) % 1000
    table = [
        [(i * 131 + k * 17 + i * i + k * k) % 1000 for k in range(M)]
        for i in range(N)
    ]

    A = [[0] * N for _ in range(N)]
    B = [[0] * N for _ in range(N)]
    MODVAL = 10**9 + 7

    for i in range(N):
        for j in range(N):
            res = MODVAL
            for k in range(M):
                diff = table[i][k] - table[j][k]
                if diff < 0:
                    diff = -diff
                if diff < res:
                    res = diff
            A[i][j] = res
            A[j][i] = res

            res = MODVAL
            for k in range(M - 1):
                diff = table[i][k] - table[j][k + 1]
                if diff < 0:
                    diff = -diff
                if diff < res:
                    res = diff
            B[i][j] = res

    dp = [[-1] * N for _ in range(1 << N)]

    sys.setrecursionlimit(1_000_000)

    def calc(mask, v):
        if dp[mask][v] != -1:
            return dp[mask][v]
        res = 0
        for u in range(N):
            if (mask & (1 << u)) and u != v:
                candidate = calc(mask ^ (1 << v), u)
                if A[u][v] < candidate:
                    candidate = A[u][v]
                if candidate > res:
                    res = candidate
        dp[mask][v] = res
        return res

    ans = 0
    full_mask = (1 << N) - 1
    for i in range(N):
        dp = [[-1] * N for _ in range(1 << N)]
        for k in range(N):
            if k == i:
                dp[1 << k][k] = MODVAL
            else:
                dp[1 << k][k] = 0
        for j in range(N):
            val = calc(full_mask, j)
            if B[j][i] < val:
                val = B[j][i]
            if val > ans:
                ans = val

    print(ans)
    return ans

if __name__ == "__main__":
    # example deterministic call
    main(4)