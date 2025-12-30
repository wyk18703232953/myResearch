def main(n):
    import random

    # 1. 根据规模 n 生成测试数据
    # 这里生成一个长度为 n 的数组 A，元素在 1..n 之间
    N = n
    A = [random.randint(1, n) for _ in range(N)]

    # 2. 将原 solve 函数逻辑封装并使用生成的数据 A, N
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = A[i]
    for X in range(2, N + 1):
        for i in range(N - X + 1):
            j = i + X - 1
            for k in range(i, j):
                if dp[i][k] == dp[k + 1][j] and dp[i][k] != -1:
                    dp[i][j] = dp[i][k] + 1
                    break

    ans = [10**9 + 1] * (N + 1)
    ans[0] = 0
    for i in range(1, N + 1):
        for k in range(1, i + 1):
            if dp[k - 1][i - 1] != -1:
                ans[i] = min(ans[i], ans[k - 1] + 1)

    return ans[N]


if __name__ == "__main__":
    # 示例：调用 main(5)
    print(main(5))