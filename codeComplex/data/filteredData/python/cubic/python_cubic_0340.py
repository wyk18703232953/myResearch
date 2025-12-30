mod = 998244353
eps = 10**-9


def main(n: int):
    """
    n: 规模参数，用于生成测试数据 A，长度为 n
    这里示例使用 A = [1, 2, ..., n] 作为测试数据，可按需要修改生成逻辑
    """
    # 生成测试数据
    A = list(range(1, n + 1)) + [0]
    A.sort()

    N = n
    dp = [[0] * (i + 1) for i in range(N + 1)]
    dp[0][0] = 1
    l = 0
    for i in range(1, N + 1):
        for ll in range(l + 1, i):
            if A[ll] * 2 <= A[i]:
                l = ll
            else:
                break
        for j in range(1, l + 2):
            dp[i][j] = (dp[l][j - 1] + (dp[i][j - 1] * (l - j + 2)) % mod) % mod
        for j in range(i):
            dp[i][j] = (dp[i - 1][j] + dp[i][j]) % mod
    print(dp[-1][-1])


# 示例：需要时可直接调用 main(n)
# main(5)