def solve(rn, gn, bn, r, g, b):
    r = sorted(r, reverse=True)
    g = sorted(g, reverse=True)
    b = sorted(b, reverse=True)

    dp = [[[0 for _ in range(bn + 1)] for _ in range(gn + 1)] for _ in range(rn + 1)]

    ans = 0
    for i in range(rn + 1):
        for j in range(gn + 1):
            for k in range(bn + 1):
                if i < rn and j < gn:
                    dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], dp[i][j][k] + r[i] * g[j])
                if i < rn and k < bn:
                    dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1], dp[i][j][k] + r[i] * b[k])
                if j < gn and k < bn:
                    dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i][j][k] + g[j] * b[k])

                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    return ans


def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    rn = n
    gn = n
    bn = n

    r = [i + 1 for i in range(rn)]
    g = [2 * (i + 1) for i in range(gn)]
    b = [3 * (i + 1) for i in range(bn)]

    ans = solve(rn, gn, bn, r, g, b)
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)