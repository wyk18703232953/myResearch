import random
from array import array

MOD = 10 ** 9 + 7

def main(n: int) -> int:
    # 1. 生成规模为 n 的测试数据：n x n 的 0/1 矩阵 edge
    #    构造为一个无向图的邻接矩阵（对称，且对角线为 0）
    random.seed(0)
    edge = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            v = random.randint(0, 1)
            edge[i][j] = v
            edge[j][i] = v

    # 2. 初始化 dp_f 和 dp_g
    # 使用 Python 列表即可，避免 array('i') * n 的坑
    dp_f = [[-1] * n for _ in range(n)]
    dp_g = [[-1] * n for _ in range(n)]

    # 对角线初始化
    for i in range(n):
        dp_f[i][i] = 1
        dp_g[i][i] = 1
    # 长度为 2 的区间初始化
    for i in range(n - 1):
        dp_f[i][i + 1] = 1 if edge[i][i + 1] else 0
        dp_g[i][i + 1] = 1 if edge[i][i + 1] else 0

    # 3. 定义递归函数 f, g，使用闭包捕获 edge, dp_f, dp_g
    def f(l: int, r: int) -> int:
        if dp_f[l][r] != -1:
            return dp_f[l][r]

        # 当 l < r 且未计算过
        dp_f[l][r] = g(l, r) if edge[l][r] else 0
        for m in range(l + 1, r):
            if edge[l][m]:
                dp_f[l][r] = (dp_f[l][r] + g(l, m) * f(m, r)) % MOD

        return dp_f[l][r]

    def g(l: int, r: int) -> int:
        if dp_g[l][r] != -1:
            return dp_g[l][r]

        dp_g[l][r] = f(l + 1, r)
        for m in range(l + 1, r):
            dp_g[l][r] = (dp_g[l][r] + f(l, m) * f(m + 1, r)) % MOD

        return dp_g[l][r]

    # 返回 f(0, n-1) 的结果
    return f(0, n - 1)


# 示例调用（评测时可忽略或删除）
if __name__ == "__main__":
    result = main(5)
    print(result)