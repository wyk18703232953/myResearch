def main(n):
    # Deterministic generation of input:
    # Original input: first line n, then n lines each "f" or not.
    # Here we generate length-n boolean list f where pattern is periodic:
    # f[i] is True if i % 3 == 0, else False. This is fully deterministic.
    f = [(i % 3 == 0) for i in range(n)]

    mod = 10**9 + 7

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
    # Example deterministic call; adjust n as needed for experiments
    main(10)