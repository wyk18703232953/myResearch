def main(n):
    # n controls the scale: n[0], n[1], n[2] are the three dimensions
    # If n is an int, use it for all three; if it's a list/tuple, take first three
    if isinstance(n, int):
        sizes = [n, n, n]

    else:
        sizes = list(n) + [0, 0, 0]
        sizes = sizes[:3]
    x, y, z = sizes

    # Deterministically generate three arrays of required lengths
    a = []
    for idx, length in enumerate((x, y, z)):
        # Example deterministic pattern depending on idx and position
        arr = [(i + 1) * (idx + 2) for i in range(length)]
        arr.sort(reverse=True)
        a.append(arr)

    dp = [[[0 for _ in range(z + 1)] for _ in range(y + 1)] for _ in range(x + 1)]
    ans = 0
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i < x and j < y:
                    val = dp[i][j][k] + a[0][i] * a[1][j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < x and k < z:
                    val = dp[i][j][k] + a[0][i] * a[2][k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if j < y and k < z:
                    val = dp[i][j][k] + a[1][j] * a[2][k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    return ans


if __name__ == "__main__":
    # Example deterministic call
    result = main(5)
    # print(result)
    pass