def main(n):
    import random

    # 生成规模为 n 的测试数据 A
    # 这里示例为在 [1, n] 范围内的随机整数，可按需要修改生成规则
    A = [random.randint(1, n) for _ in range(n)]

    N = n
    dp = [[0] * N for _ in range(N)]
    for j in range(N):
        dp[j][0] = A[j]

    for l in range(1, N):
        for j in range(l, N):
            for k in range(j - l, j):
                if dp[k][k - j + l] == dp[j][j - k - 1] > 0:
                    dp[j][l] = 1 + dp[j][j - k - 1]
                    break

    dp = [None] + dp
    Dp = [0] * (N + 1)
    for j in range(1, N + 1):
        res = N
        for l in range(j):
            if dp[j][l]:
                res = min(res, 1 + Dp[j - l - 1])
        Dp[j] = res

    # 输出结果
    print(Dp[N])


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时按需修改 n
    main(5)