def main(n):
    # n is the base size; map it to three sizes
    # Ensure positive sizes for meaningful DP
    x = max(1, n)
    n0 = x
    n1 = x + 1
    n2 = x + 2
    sizes = [n0, n1, n2]

    # Generate deterministic arrays for a[0], a[1], a[2]
    a = []
    for idx, sz in enumerate(sizes):
        arr = []
        for i in range(sz):
            # Deterministic arithmetic construction depending on idx and i
            val = (idx + 1) * (i + 1) + (i * i) // (idx + 2)
            arr.append(val)
        arr.sort(reverse=True)
        a.append(arr)

    dp = [[[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)] for _ in range(n0 + 1)]
    ans = 0
    for i in range(n0 + 1):
        for j in range(n1 + 1):
            for k in range(n2 + 1):
                if i < n0 and j < n1:
                    dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], dp[i][j][k] + a[0][i] * a[1][j])
                if i < n0 and k < n2:
                    dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1], dp[i][j][k] + a[0][i] * a[2][k])
                if j < n1 and k < n2:
                    dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i][j][k] + a[1][j] * a[2][k])
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)