def main(n):
    # 生成测试数据：长度为 n 的数组 a
    # 这里示例使用 1..n 的递增序列，可按需要修改生成规则
    a = list(range(1, n + 1))

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 预处理 dp
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = a[i]
            elif i == j - 1:
                if a[i] == a[j]:
                    dp[i][j] = a[i] + 1
            else:
                for k in range(i, j):
                    if dp[i][k] and dp[k + 1][j] and dp[i][k] == dp[k + 1][j]:
                        dp[i][j] = dp[i][k] + 1
                        break

    INF = 10 ** 18
    ans = [INF] * (n + 1)
    ans[-1] = 0

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if dp[i][j]:
                ans[i] = min(ans[i], 1 + ans[j + 1])
            else:
                ans[i] = min(ans[i], j - i + 1 + ans[j + 1])

    # 输出结果
    print(ans[0])


# 示例调用
if __name__ == "__main__":
    main(5)