def main(n):
    if n <= 0:
        r = g = b = 0

    else:
        r = n
        g = n
        b = n

    sticks = []
    # deterministic generation: decreasing sequences per color
    red = sorted([(i * 2 + 1) % (3 * n + 1 if n > 0 else 1) for i in range(r)], reverse=True)
    green = sorted([(i * 3 + 2) % (3 * n + 1 if n > 0 else 1) for i in range(g)], reverse=True)
    blue = sorted([(i * 5 + 4) % (3 * n + 1 if n > 0 else 1) for i in range(b)], reverse=True)
    sticks.append(red)
    sticks.append(green)
    sticks.append(blue)

    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
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
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    main(3)