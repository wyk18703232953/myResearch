def main(n):
    # n is the length of the array aa
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministically generate the input array of length n
    # Example pattern: aa[i] = (i % 5) + 1
    aa = [(i % 5) + 1 for i in range(n)]

    dp = [[0] * (n + 1) for _ in range(n)]

    def calc_dp(i, j):
        if i + 1 == j:
            dp[i][j] = aa[i]
        if dp[i][j] != 0:
            return dp[i][j]
        dp[i][j] = -1
        for k in range(i + 1, j):
            lf = calc_dp(i, k)
            rg = calc_dp(k, j)
            if lf > 0 and lf == rg:
                dp[i][j] = lf + 1
                break
        return dp[i][j]

    dp2 = list(range(0, n + 1))
    for i in range(n):
        for j in range(i + 1, n + 1):
            if calc_dp(i, j) > 0:
                dp2[j] = min(dp2[j], dp2[i] + 1)
    # print(dp2[n])
    pass
if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)