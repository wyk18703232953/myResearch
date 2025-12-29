import random

INF = 10000


def main(n: int):
    # 生成规模为 n 的测试数据：aa 为长度为 n 的正整数序列
    # 可根据需要调整数据范围
    random.seed(0)
    aa = [random.randint(1, 5) for _ in range(n)]

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

    # 输出结果（以及可选的测试数据）
    print(dp2[n])
    # 如需查看测试数据，可取消下一行注释
    # print("aa =", aa)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)