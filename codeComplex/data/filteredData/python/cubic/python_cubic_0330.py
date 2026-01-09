def main(n):
    # Interpret n as the common size of three arrays R, G, B
    R = G = B = n

    # Deterministic data generation based on n
    red = [(i * 2 + 1) for i in range(R)]
    green = [(i * 3 + 2) for i in range(G)]
    blue = [(i * 5 + 3) for i in range(B)]

    red.sort(reverse=True)
    green.sort(reverse=True)
    blue.sort(reverse=True)

    NEG_INF = -2 * 10**9
    dp = [[[-10**18] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]
    dp[0][0][0] = 0
    ans = 0

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                cur = dp[i][j][k]
                if i > 0 and j > 0:
                    cur = max(cur, dp[i - 1][j - 1][k] + red[i - 1] * green[j - 1])
                if j > 0 and k > 0:
                    cur = max(cur, dp[i][j - 1][k - 1] + green[j - 1] * blue[k - 1])
                if i > 0 and k > 0:
                    cur = max(cur, dp[i - 1][j][k - 1] + red[i - 1] * blue[k - 1])
                dp[i][j][k] = cur
                if cur > ans:
                    ans = cur

    # print(ans)
    pass
if __name__ == "__main__":
    main(5)