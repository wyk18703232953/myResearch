def main(n):
    from collections import defaultdict

    # 输入规模映射：
    # n 作为 N（序列长度），同时生成一个确定性的整数序列 X
    # X[i] = (i * 2 + 3) % (n + 7) 保证不同 n 下数据随规模变化且完全确定
    if n <= 0:
        # print(0)
        pass
        return

    N = n
    X = [(i * 2 + 3) % (n + 7) for i in range(N)]

    dp = defaultdict(lambda: -1)
    M = 1000

    for i in range(N):
        dp[i + M] = X[i]

    for i in range(2, N + 1):
        for j in range(N - i + 1):
            for k in range(1, i):
                u, v = dp[j + M * k], dp[j + k + M * (i - k)]
                if u == -1 or v == -1 or u != v:
                    continue
                dp[j + M * i] = u + 1
                break

    dp2 = [0] * (N + 1)
    for i in range(N):
        dp2[i + 1] = dp2[i] + 1
        for j in range(i + 1):
            if dp[j + (i + 1 - j) * M] == -1:
                continue
            dp2[i + 1] = min(dp2[i + 1], dp2[j] + 1)
    # print(dp2[-1])
    pass
if __name__ == "__main__":
    # 示例调用：可修改 n 以进行不同规模的时间复杂度实验
    main(10)