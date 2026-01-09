def main(n):
    # Map n to problem sizes: split n into three parts as evenly as possible
    x = n // 3
    y = (n + 1) // 3
    z = n - x - y
    n_list = [x, y, z]

    # Deterministic data generation
    a = []
    # For each of the three arrays, generate values in a simple deterministic pattern
    for idx in range(3):
        length = n_list[idx]
        # Example deterministic generation: descending sequence based on index and position
        arr = [ (length - i) * (idx + 1) for i in range(length) ]
        # Original code sorts in reverse; this construction is already non-increasing, but keep sort to preserve logic
        arr.sort(reverse=True)
        a.append(arr)

    # DP dimensions based on n_list
    x_len, y_len, z_len = n_list
    dp = [[[0 for _ in range(z_len + 1)] for _ in range(y_len + 1)] for _ in range(x_len + 1)]
    ans = 0

    for i in range(x_len + 1):
        for j in range(y_len + 1):
            for k in range(z_len + 1):
                if i < x_len and j < y_len:
                    val = dp[i][j][k] + a[0][i] * a[1][j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < x_len and k < z_len:
                    val = dp[i][j][k] + a[0][i] * a[2][k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if j < y_len and k < z_len:
                    val = dp[i][j][k] + a[1][j] * a[2][k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]

    # print(ans)
    pass
if __name__ == "__main__":
    main(9)