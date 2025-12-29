import random

def main(n: int):
    # 生成测试数据：长度为 n 的数组 a，元素为 1~n 的随机整数
    a = [random.randint(1, n) for _ in range(n)]

    dp = [[505] * n for _ in range(n)]
    Max = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
        Max[i][i] = a[i]

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                if dp[i][k] == 1 and dp[k + 1][j] == 1 and Max[i][k] == Max[k + 1][j]:
                    dp[i][j] = 1
                    Max[i][j] = Max[i][k] + 1

    print(dp[0][n - 1])


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)