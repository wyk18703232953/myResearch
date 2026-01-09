def main(n):
    mod = 10**9 + 7

    # Deterministic generation of f: alternate True/False
    f = [(i % 2 == 0) for i in range(n)]

    def summ(a, b):
        return (a + b) % mod

    dp = [1]
    for ii in range(1, n):
        pf = f[ii - 1]
        if pf:
            dp.insert(0, 0)

        else:
            for jj in reversed(range(1, len(dp))):
                dp[jj - 1] = summ(dp[jj - 1], dp[jj])

    ans = 0
    for vv in dp:
        ans = summ(ans, vv)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)