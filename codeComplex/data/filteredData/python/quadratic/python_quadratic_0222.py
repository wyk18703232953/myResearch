def main(n):
    # n 表示数组长度
    if n <= 0:
        print(-1)
        return

    # 确定性生成输入数据
    # a 为严格递增序列，确保存在递增三元组
    a = [i + 1 for i in range(n)]
    # b 为某个简单规则构造的代价数组
    b = [(i * 3 + 1) % 10 + 1 for i in range(n)]

    PI = float('inf')
    ans = PI
    dp = [[PI for _ in range(4)] for _ in range(n)]

    for i in range(n):
        dp[i][1] = b[i]
        for j in range(i):
            if a[j] < a[i]:
                dp[i][2] = min(dp[i][2], dp[j][1] + b[i])
                dp[i][3] = min(dp[i][3], dp[j][2] + b[i])
                ans = min(ans, dp[i][3])

    print(ans if ans != PI else -1)


if __name__ == "__main__":
    main(10)