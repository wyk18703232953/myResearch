def main(n):
    # n controls the size of each color array; original code expects three sizes
    # Map single integer n -> [n, n, n]
    sizes = [n, n, n]

    # deterministic data generation for a[0], a[1], a[2]
    a = []
    for color in range(3):
        length = sizes[color]
        # simple deterministic sequence depending on color and index
        arr = [color * 10 + i for i in range(1, length + 1)]
        arr.sort(reverse=True)
        a.append(arr)

    r, g, b = sizes
    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i < r and j < g:
                    v = dp[i][j][k] + a[0][i] * a[1][j]
                    if v > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = v
                if i < r and k < b:
                    v = dp[i][j][k] + a[0][i] * a[2][k]
                    if v > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = v
                if j < g and k < b:
                    v = dp[i][j][k] + a[1][j] * a[2][k]
                    if v > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = v
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    return ans

if __name__ == "__main__":
    # example call for time-complexity experiments
    n = 5
    result = main(n)
    # print(result)
    pass