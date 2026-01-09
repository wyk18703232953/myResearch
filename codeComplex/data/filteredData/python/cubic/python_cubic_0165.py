def main(n):
    inf = 10 ** 9

    # deterministically generate input array aa of length n
    # use a simple periodic pattern so values are small but non-trivial
    aa = [(i % 3) + 1 for i in range(n)]

    dp1 = [[-1] * n for _ in range(n)]
    dp2 = [[inf] * n for _ in range(n)]

    for i in range(n):
        dp1[i][i] = aa[i]
        dp2[i][i] = 1

    for w in range(2, n + 1):
        for l in range(n - w + 1):
            r = l + w - 1
            for m in range(l, r):
                if dp1[l][m] != -1 and dp1[l][m] == dp1[m + 1][r]:
                    dp1[l][r] = dp1[l][m] + 1
                    dp2[l][r] = 1

    for m in range(n):
        for l in range(m + 1):
            for r in range(m + 1, n):
                dp2[l][r] = min(dp2[l][r], dp2[l][m] + dp2[m + 1][r])

    # print(dp2[0][n - 1])
    pass
if __name__ == "__main__":
    # example deterministic call for experimental use
    main(10)