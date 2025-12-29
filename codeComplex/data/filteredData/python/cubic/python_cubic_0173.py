import random

def main(n: int):
    # 生成规模为 n 的测试数据 A
    # 这里生成 1~3 之间的随机整数，可按需要修改生成策略
    random.seed(0)
    A = [random.randint(1, 3) for _ in range(n)]

    INF = 10**3
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    # dp[i][j]: 区间 [i, j) 的操作后长度的最小值
    val = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        dp[i][i + 1] = 1
        val[i][i + 1] = A[i]

    for d in range(2, n + 1):
        for i in range(n + 1 - d):
            j = i + d
            for k in range(i + 1, j):
                if dp[i][k] == 1 and dp[k][j] == 1 and val[i][k] == val[k][j]:
                    dp[i][j] = min(dp[i][j], 1)
                    val[i][j] = val[i][k] + 1
                else:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    print(dp[0][n])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)