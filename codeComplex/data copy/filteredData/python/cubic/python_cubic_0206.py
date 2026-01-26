def main(n):
    # Map n to sizes of the three arrays; keep them similar scale
    # Ensure at least size 1 for non-trivial behavior
    r = max(1, n // 3)
    g = max(1, n // 3)
    b = max(1, n - r - g)
    # Deterministic data generation
    rs = sorted([(i * 2 + 1) % 1000003 for i in range(r)])
    gs = sorted([(i * 3 + 2) % 1000003 for i in range(g)])
    bs = sorted([(i * 5 + 3) % 1000003 for i in range(b)])
    # Core DP logic unchanged
    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i > 0 and k > 0:
                    val = dp[i - 1][j][k - 1] + rs[i - 1] * bs[k - 1]
                    if val > dp[i][j][k]:
                        dp[i][j][k] = val
                if i > 0 and j > 0:
                    val = dp[i - 1][j - 1][k] + rs[i - 1] * gs[j - 1]
                    if val > dp[i][j][k]:
                        dp[i][j][k] = val
                if j > 0 and k > 0:
                    val = dp[i][j - 1][k - 1] + gs[j - 1] * bs[k - 1]
                    if val > dp[i][j][k]:
                        dp[i][j][k] = val
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    # print(ans)
    pass
if __name__ == "__main__":
    main(30)