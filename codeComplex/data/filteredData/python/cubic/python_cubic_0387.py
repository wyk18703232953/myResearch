import math

DEBUG = 0

def main(n):
    """
    n: 问题规模
    返回：程序原本对给定 n 和模数 M 的输出结果
    这里选择一个固定的大质数作为 M 来生成测试数据。
    """
    # 生成测试数据：固定一个大质数作为模数
    M = 10**9 + 7

    f = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    comb = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    fact = [0] * (n + 1)
    inv = [0] * (n + 1)
    fact[0] = inv[0] = 1

    # 预处理阶乘及其逆元
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % M
        inv[i] = pow(fact[i], M - 2, M)

    # 组合数 C(i, j)
    for i in range(0, n + 1):
        for j in range(0, i + 1):
            comb[i][j] = ((fact[i] * inv[j]) % M * inv[i - j]) % M

    # 预处理 2 的幂
    pow2 = [0] * (n + 1)
    pow2[0] = 1
    for i in range(1, n + 1):
        pow2[i] = pow2[i - 1] * 2 % M
        f[i][i] = pow2[i - 1]

    # DP 计算 f[total][manual]
    for total in range(1, n + 1):
        for manual in range(1, total):
            if total > manual * 2 or total < manual:
                continue
            for l in range(1, manual):
                f[total][manual] += (
                    f[total - l - 1][manual - l]
                    * pow2[l - 1]
                    * comb[manual][l]
                )
                f[total][manual] %= M

    c = 0
    for i in range(1, n + 1):
        c += f[n][i]

    ans = c % M
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)