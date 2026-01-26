def main(n):
    # Interpret n as the base size for three arrays
    # Original code reads 3 sizes in n[0], n[1], n[2]
    # Here we deterministically derive them from n
    n0 = n
    n1 = max(1, n // 2)
    n2 = max(1, (n * 3) // 4)
    sizes = [n0, n1, n2]

    a = []
    # Deterministic generation of three arrays with given sizes
    for idx, sz in enumerate(sizes):
        # Example deterministic pattern: arithmetic function of index and position
        arr = [(i * (idx + 1) + idx * idx) % (10 * (idx + 1) + 7) + i for i in range(sz)]
        arr.sort(reverse=True)
        a.append(arr)

    dp = [[[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)] for _ in range(n0 + 1)]
    ans = 0
    for i in range(n0 + 1):
        for j in range(n1 + 1):
            for k in range(n2 + 1):
                if i < n0 and j < n1:
                    val = dp[i][j][k] + a[0][i] * a[1][j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < n0 and k < n2:
                    val = dp[i][j][k] + a[0][i] * a[2][k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if j < n1 and k < n2:
                    val = dp[i][j][k] + a[1][j] * a[2][k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)