def main(n):
    # Interpret n as the size for r, g, b and corresponding lists
    r = n
    g = n
    b = n

    # Deterministically generate s1, s2, s3 based on n
    s1 = [i + 1 for i in range(r)]
    s2 = [2 * (i + 1) for i in range(g)]
    s3 = [3 * (i + 1) for i in range(b)]

    s1.sort()
    s2.sort()
    s3.sort()
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    s1 = [0] + s1
    s2 = [0] + s2
    s3 = [0] + s3

    dp = []
    for i in range(r + 5):
        H = []
        for j in range(g + 5):
            h = []
            for k in range(b + 5):
                h.append(0)
            H.append(h)
        dp.append(H)

    for i in range(0, r + 1):
        for j in range(0, g + 1):
            for k in range(0, b + 1):
                t1, t2, t3, t4, t5, t6 = 0, 0, 0, 0, 0, 0
                if i - 1 >= 0 and j - 1 >= 0:
                    t1 = dp[i - 1][j - 1][k] + (s1[i] * s2[j])
                if i - 1 >= 0 and k - 1 >= 0:
                    t2 = dp[i - 1][j][k - 1] + (s1[i] * s3[k])
                if k - 1 >= 0 and j - 1 >= 0:
                    t3 = dp[i][j - 1][k - 1] + (s2[j] * s3[k])
                if i - 1 >= 0:
                    t4 = dp[i - 1][j][k]
                if j - 1 >= 0:
                    t5 = dp[i][j - 1][k]
                if k - 1 >= 0:
                    t6 = dp[i][j][k - 1]

                dp[i][j][k] = max(t1, t2, t3, t4, t5, t6)

    result = dp[r][g][b]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(3)