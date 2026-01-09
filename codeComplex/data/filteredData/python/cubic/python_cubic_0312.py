def main(n):
    global ans, dp, R, G, B, r, g, b
    ans = 0

    # Map n to sizes of three arrays so total state ~ O(n)
    # R + G + B ≈ n, here R = n, G = n//2, B = n//3 (at least 1)
    R = max(1, n)
    G = max(1, n // 2)
    B = max(1, n // 3)

    # Deterministic data generation
    # Values grow with index to make the DP do real work
    r = [(i * 3 + 1) % 1000003 for i in range(R)]
    g = [(i * 5 + 2) % 1000003 for i in range(G)]
    b = [(i * 7 + 3) % 1000003 for i in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    dp = [[[-1 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    def rec(i, j, k):
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        x1 = x2 = x3 = 0
        if i < R and j < G:
            x1 = r[i] * g[j] + rec(i + 1, j + 1, k)
        if i < R and k < B:
            x2 = r[i] * b[k] + rec(i + 1, j, k + 1)
        if j < G and k < B:
            x3 = g[j] * b[k] + rec(i, j + 1, k + 1)
        val = max(x1, x2, x3)
        dp[i][j][k] = val
        nonlocal ans
        if val > ans:
            ans = val
        return val

    rec(0, 0, 0)
    # print(ans)
    pass
if __name__ == "__main__":
    main(30)