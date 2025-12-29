def main(n):
    # 生成测试数据：根据规模 n 构造 N, M
    # 这里简单设置 N = n, M 为一个大素数模数
    N = n
    M = 10**9 + 7

    # 以下函数均依赖于 N, M，因此在 main 内部定义并使用闭包变量

    def powers(limit):
        size = limit + 1
        p = [1] * size
        for i in range(1, size):
            p[i] = (2 * p[i - 1]) % M
        return p

    def binomials(limit):
        size = limit + 1
        bc = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            bc[i][0] = 1
        for i in range(1, size):
            for k in range(1, i + 1):
                bc[i][k] = (bc[i - 1][k - 1] + bc[i - 1][k]) % M
        return bc

    BC = binomials(N)
    POW = powers(N)

    def solve():
        size = N + 1
        dp = [[0 for _ in range(size)] for _ in range(size)]
        dp[1][0] = 1

        for i in range(2, size):
            for k in range(1, i):
                for j in range(1, k):
                    dp[i][j] += BC[i - j][k - j] * dp[k - 1][j - 1] * POW[i - k - 1]
                    dp[i][j] %= M
            dp[i][0] = POW[i - 1]

        res = 0
        for j in range(0, N - 1):
            res = (res + dp[N][j]) % M
        return res

    return solve()


# 示例：如果需要直接运行，可取消下面两行注释
# if __name__ == "__main__":
#     print(main(5))