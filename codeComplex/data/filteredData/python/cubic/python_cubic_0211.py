def main(n):
    # Interpret n as the size of each color group: r = g = b = n
    r = g = b = n

    # Deterministic generation of stick lengths:
    # Three sequences of length n, constructed via simple arithmetic
    red = [i + 1 for i in range(r)]
    green = [2 * (i + 1) for i in range(g)]
    blue = [3 * (i + 1) for i in range(b)]

    # Original code sorts each list in descending order
    sticks = [
        sorted(red, reverse=True),
        sorted(green, reverse=True),
        sorted(blue, reverse=True),
    ]

    # Allocate 3D DP table: dp[i][j][k] for i red, j green, k blue used
    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
                if i < r and j < g:
                    val = dp[i][j][k] + sticks[0][i] * sticks[1][j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < r and k < b:
                    val = dp[i][j][k] + sticks[0][i] * sticks[2][k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if j < g and k < b:
                    val = dp[i][j][k] + sticks[1][j] * sticks[2][k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val

    # print(ans)
    pass
if __name__ == "__main__":
    main(3)