def main(n):
    r = n % 201
    g = (2 * n + 3) % 201
    b = (3 * n + 5) % 201
    if r == 0:
        r = 1
    if g == 0:
        g = 1
    if b == 0:
        b = 1

    ra = [((i * 7 + 3) % 1000) + 1 for i in range(r)]
    ga = [((i * 5 + 11) % 1000) + 1 for i in range(g)]
    ba = [((i * 9 + 17) % 1000) + 1 for i in range(b)]

    ra.sort()
    ga.sort()
    ba.sort()

    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                val = dp[i][j][k]
                if i > 0 and j > 0:
                    tmp = dp[i - 1][j - 1][k] + ra[i - 1] * ga[j - 1]
                    if tmp > val:
                        val = tmp
                if i > 0 and k > 0:
                    tmp = dp[i - 1][j][k - 1] + ra[i - 1] * ba[k - 1]
                    if tmp > val:
                        val = tmp
                if j > 0 and k > 0:
                    tmp = dp[i][j - 1][k - 1] + ga[j - 1] * ba[k - 1]
                    if tmp > val:
                        val = tmp
                dp[i][j][k] = val

    # print(dp[r][g][b])
    pass
if __name__ == "__main__":
    main(50)