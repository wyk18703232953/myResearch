import random

# 全局变量声明（与原程序保持一致）
r = g = b = None
dp = None


def func(n1, n2, n3):
    global r, g, b, dp
    if ((n1 < 0 and n2 < 0) or (n3 < 0 and n2 < 0) or (n1 < 0 and n3 < 0)):
        return 0
    if n1 < 0:
        return g[n2] * b[n3] + func(n1, n2 - 1, n3 - 1)
    if n2 < 0:
        return r[n1] * b[n3] + func(n1 - 1, n2, n3 - 1)
    if n3 < 0:
        return g[n2] * r[n1] + func(n1 - 1, n2 - 1, n3)
    if dp[n1][n2][n3] == -1:
        dp[n1][n2][n3] = max(
            g[n2] * b[n3] + func(n1, n2 - 1, n3 - 1),
            r[n1] * b[n3] + func(n1 - 1, n2, n3 - 1),
            g[n2] * r[n1] + func(n1 - 1, n2 - 1, n3),
        )
    return dp[n1][n2][n3]


def main(n):
    """
    n 为规模参数，用于生成 R,G,B 的大小。
    这里简单设定：R = G = B = n。
    """
    global r, g, b, dp

    R = G = B = n

    # 生成测试数据：1 到 100 之间的随机整数
    r = sorted(random.randint(1, 100) for _ in range(R))
    g = sorted(random.randint(1, 100) for _ in range(G))
    b = sorted(random.randint(1, 100) for _ in range(B))

    # 原代码中前缀数组并未在 func 中使用，这里保留生成逻辑但不强制使用
    prefix1 = [0] * R
    prefix2 = [0] * G
    prefix3 = [0] * B
    prefix1[0] = r[0]
    prefix2[0] = g[0]
    prefix3[0] = b[0]

    # 三维 dp 初始化为 -1
    dp = [[[-1 for _ in range(B)] for _ in range(G)] for _ in range(R)]

    result = func(R - 1, G - 1, B - 1)
    print(result)


if __name__ == "__main__":
    # 示例：n = 3，可根据需要修改
    main(3)