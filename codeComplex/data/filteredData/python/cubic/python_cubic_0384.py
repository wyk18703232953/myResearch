def main(n):
    """
    n: 问题规模，用来生成测试数据 (N, M)
       这里示例生成：
       N = n
       M = 一个稍大的质数 10**9+7，避免模数太小
    返回：原 solve() 的计算结果（字符串）
    """

    # 根据 n 生成测试数据
    N = n
    M = 10**9 + 7

    # 预处理：2 的幂
    def powers(limit, M):
        size = limit + 1
        p = [1] * size
        for i in range(1, size):
            p[i] = 2 * p[i - 1] % M
        return p

    # 预处理：二项式系数 C(n, k) mod M
    def binomials(limit, M):
        size = limit + 1
        bc = [[0] * size for _ in range(size)]
        for i in range(size):
            bc[i][0] = 1
        for i in range(1, size):
            for k in range(1, i + 1):
                bc[i][k] = (bc[i - 1][k - 1] + bc[i - 1][k]) % M
        return bc

    BC = binomials(N, M)
    POW = powers(N, M)

    # 主逻辑 (原 solve)
    def solve(N, M, BC, POW):
        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp[0][0] = 1

        for i in range(1, N):
            for k in range(1, i):
                for j in range(1, i):
                    dp[i][j] += BC[j + 1][i - k] * dp[k - 1][j - 1 - (i - k - 1)] * POW[i - k - 1]
                    dp[i][j] %= M
            dp[i][i] = POW[i]

        res = 0
        for j in range(N):
            res = (res + dp[N - 1][j]) % M
        return str(res)

    return solve(N, M, BC, POW)


# 示例：直接运行本文件时做一次调用
if __name__ == "__main__":
    # 例如取 n = 5 做测试
    print(main(5))