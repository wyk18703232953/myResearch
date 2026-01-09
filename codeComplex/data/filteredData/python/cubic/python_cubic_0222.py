#!/usr/bin/env python3

def main(n):
    # Map n to sizes of three arrays; keep total size O(n)
    R = max(1, n)
    G = max(1, n // 2 if n >= 2 else 1)
    B = max(1, n // 3 if n >= 3 else 1)

    # Deterministic data generation
    r = [(i * 2 + 1) % 100000 for i in range(R)]
    g = [(i * 3 + 2) % 100000 for i in range(G)]
    b = [(i * 5 + 3) % 100000 for i in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    nr = len(r)
    ng = len(g)
    nb = len(b)

    dp = [[[0] * (nb + 1) for _ in range(ng + 1)] for _ in range(nr + 1)]
    ans = 0
    for i in range(nr + 1):
        for j in range(ng + 1):
            for k in range(nb + 1):
                if (i + j + k) % 2 == 1:
                    continue
                if i > 0 and j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1])
                if j > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1])
                if i > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1] + b[k - 1] * r[i - 1])
                ans = max(ans, dp[i][j][k])

    # print(ans)
    pass
if __name__ == "__main__":
    # Example: run with a chosen scale n
    main(10)