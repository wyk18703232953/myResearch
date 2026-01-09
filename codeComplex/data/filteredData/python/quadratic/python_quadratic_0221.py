def main(n: int):
    # 生成测试数据：a 为严格递增数组，b 为从 1 到 n 的正整数
    a = list(range(1, n + 1))
    b = list(range(1, n + 1))

    dp = [0] * n
    for i in range(n):
        v = float('inf')
        for j in range(i + 1, n):
            if a[j] > a[i]:
                v = min(v, b[i] + b[j])
        dp[i] = v

    for i in range(n):
        v = float('inf')
        for j in range(i + 1, n):
            if a[j] > a[i]:
                v = min(v, b[i] + dp[j])
        dp[i] = v

    ans = min(dp)
    # print(ans if ans != float('inf') else -1)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)