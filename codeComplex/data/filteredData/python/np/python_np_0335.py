import sys

def main(n):
    if n <= 1:
        print(0)
        return

    # Define N and M based on n to scale the input deterministically
    N = n
    M = max(1, n // 2)

    # Deterministic construction of table: table[i][k] is a simple function of i,k
    table = [[i * 1000 + k * 7 for k in range(M)] for i in range(N)]

    A = [[0] * N for _ in range(N)]
    B = [[0] * N for _ in range(N)]
    INF = 10 ** 9 + 7

    for i in range(N):
        for j in range(N):
            res = INF
            for k in range(M):
                diff = table[i][k] - table[j][k]
                if diff < 0:
                    diff = -diff
                if diff < res:
                    res = diff
            A[i][j] = res
            A[j][i] = res

            res = INF
            if M > 1:
                for k in range(M - 1):
                    diff = table[i][k] - table[j][k + 1]
                    if diff < 0:
                        diff = -diff
                    if diff < res:
                        res = diff
            B[i][j] = res

    dp = [[-1] * N for _ in range(1 << N)]

    def calc(mask, v):
        if dp[mask][v] != -1:
            return dp[mask][v]
        res = 0
        for u in range(N):
            if (mask & (1 << u)) and u != v:
                val = calc(mask ^ (1 << v), u)
                if A[u][v] < val:
                    val = A[u][v]
                if val > res:
                    res = val
        dp[mask][v] = res
        return res

    ans = 0
    full_mask = (1 << N) - 1
    for i in range(N):
        dp = [[-1] * N for _ in range(1 << N)]
        for k in range(N):
            if k == i:
                dp[1 << k][k] = INF
            else:
                dp[1 << k][k] = 0
        for j in range(N):
            val1 = B[j][i]
            val2 = calc(full_mask, j)
            if val1 > val2:
                cur = val2
            else:
                cur = val1
            if cur > ans:
                ans = cur

    print(ans)

if __name__ == "__main__":
    main(4)