def main(n):
    INF = 10000

    # 确定性生成输入数据：长度为 n 的整数数组 aa
    # 示例构造：aa[i] = (i % 5) + 1，保证均为正数，且有一定重复结构
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
    # 示例：使用 n = 10 作为输入规模，可按需修改或在外部多次调用 main(n)
    main(10)