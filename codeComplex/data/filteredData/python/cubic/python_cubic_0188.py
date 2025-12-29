import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组 a
    # 为方便合并（值会累加），用较小的正整数
    a = [random.randint(1, 3) for _ in range(n)]

    maxn = 600  # 与原程序保持一致上限
    new_a = [[0] * maxn for _ in range(maxn)]
    dp = [[0x7fffffff] * maxn for _ in range(maxn)]

    # 初始化
    for i in range(n):
        new_a[i + 1][i + 1] = a[i]
        dp[i + 1][i + 1] = 1

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            dp[i][j] = j - i + 1

    # 区间 DP
    for llen in range(2, n + 1):
        for left in range(1, n - llen + 2):
            right = left + llen - 1
            for middle in range(left, right):
                dp[left][right] = min(dp[left][right],
                                      dp[left][middle] + dp[middle + 1][right])
                if (dp[left][middle] == 1 and
                    dp[middle + 1][right] == 1 and
                    new_a[left][middle] == new_a[middle + 1][right]):
                    dp[left][right] = 1
                    new_a[left][right] = new_a[left][middle] + 1

    print(dp[1][n])


if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)