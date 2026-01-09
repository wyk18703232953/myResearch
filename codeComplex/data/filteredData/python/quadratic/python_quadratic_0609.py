def max_sub(arr, n):
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
    return max(0, max(dp))


def main(n):
    import math

    # 映射规模：n 为数组长度，同时用于控制 m 和 k 的大小
    if n <= 0:
        return

    # 确定性生成 n, m, k
    N = n
    m = max(1, (n % 10) + 1)  # 1 到 10 之间
    k = (n // 2) + 3

    # 生成数组 arr，长度为 N
    # 使用简单算术构造，包含正负混合
    arr = [((i * 2) % 11) - 5 for i in range(N)]

    q = -math.inf
    dp = [[q] * 11 for _ in range(300100)]

    if m == 1:
        for i in range(N):
            arr[i] = arr[i] - k
        result = max_sub(arr, N)
        # print(result)
        pass

    else:
        for i in range(N):
            dp[i][1] = arr[i] - k
            for j in range(m):
                if i - 1 < 0 or dp[i - 1][j] == q:
                    continue
                nxt = (j + 1) % m
                if nxt != 1:
                    dp[i][nxt] = dp[i - 1][j] + arr[i]

                else:
                    dp[i][nxt] = max(arr[i] - k, dp[i - 1][j] + arr[i] - k)
        ma = 0
        for i in range(N):
            for j in range(m):
                ma = max(ma, dp[i][j])
        # print(ma)
        pass
if __name__ == "__main__":
    # 示例调用：可修改 n 来进行规模化实验
    main(1000)