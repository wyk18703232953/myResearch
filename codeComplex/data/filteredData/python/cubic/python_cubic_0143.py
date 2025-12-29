import random

def main(n):
    # 生成测试数据 a：长度为 n 的整数数组
    # 这里选取元素在 1~3 范围内，便于产生可合并的区间
    a = [random.randint(1, 3) for _ in range(n)]

    INF = 10 ** 9
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    val = [[-1] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        dp[i][i + 1] = 1
        val[i][i + 1] = a[i]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l
            for k in range(i + 1, j):
                if dp[i][k] == 1 and dp[k][j] == 1 and val[i][k] == val[k][j]:
                    dp[i][j] = 1
                    val[i][j] = val[i][k] + 1
                else:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    print(dp[0][n])


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)