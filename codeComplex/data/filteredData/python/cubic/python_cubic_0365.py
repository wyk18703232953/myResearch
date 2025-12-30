import sys

sys.setrecursionlimit(10**5)


def main(n: int):
    # 生成测试数据：根据规模 n 生成模数 md
    # 这里简单设定为一个大质数，常用于组合数取模
    md = 10**9 + 7

    # 组合数相关函数，在内部使用闭包访问 fac, ifac, md
    def nCr(com_n, com_r):
        if com_r < 0:
            return 0
        if com_n < com_r:
            return 0
        return fac[com_n] * ifac[com_r] % md * ifac[com_n - com_r] % md

    # 预处理阶乘与逆元
    # 原代码中 n_max = 405，这里保持一致（假设 n 不超过 400）
    n_max = 405
    fac = [1]
    for i in range(1, n_max + 1):
        fac.append(fac[-1] * i % md)
    ifac = [1] * (n_max + 1)
    ifac[n_max] = pow(fac[n_max], md - 2, md)
    for i in range(n_max - 1, 1, -1):
        ifac[i] = ifac[i + 1] * (i + 1) % md

    # 预处理 2 的幂
    pw = [1]
    for _ in range(400):
        pw.append(pw[-1] * 2 % md)

    # dp[i][j]...iにj個目の白を置いたときの場合の数
    dp = [[0] * (n // 2 + 2) for _ in range(n + 2)]
    dp[0][0] = 1
    for i in range(1, n + 2):
        for j in range(1, n // 2 + 2):
            v = 0
            for k in range(i - 2, -1, -1):
                v += dp[k][j - 1] * pw[i - k - 2] * nCr(i - j, i - k - 1) % md
            dp[i][j] = v % md

    ans = sum(dp[-1]) % md
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10)