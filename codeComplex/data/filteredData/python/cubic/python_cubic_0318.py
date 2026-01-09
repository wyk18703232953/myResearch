def main(n):
    # Map n to sizes of the three color arrays in a simple deterministic way
    r = n
    g = n
    b = n

    # Deterministic generation of color values
    red = [(i * 2 + 1) for i in range(r)]
    green = [(i * 3 + 2) for i in range(g)]
    blue = [(i * 5 + 3) for i in range(b)]

    red.sort()
    green.sort()
    blue.sort()

    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i > 0 and j > 0:
                    v = dp[i - 1][j - 1][k] + red[i - 1] * green[j - 1]
                    if v > dp[i][j][k]:
                        dp[i][j][k] = v
                if i > 0 and k > 0:
                    v = dp[i - 1][j][k - 1] + red[i - 1] * blue[k - 1]
                    if v > dp[i][j][k]:
                        dp[i][j][k] = v
                if j > 0 and k > 0:
                    v = dp[i][j - 1][k - 1] + green[j - 1] * blue[k - 1]
                    if v > dp[i][j][k]:
                        dp[i][j][k] = v

    # print(dp[-1][-1][-1])
    pass
if __name__ == "__main__":
    main(3)