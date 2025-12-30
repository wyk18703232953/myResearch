import random


def main(n):
    # 生成规模参数：
    # n: 行数
    # m: 列数（这里设为 n，若需要可改为其它函数关系）
    # k: 步数参数（偶数），这里设置为 2 * n（可按需调整）
    m = n
    k = 2 * n
    if k % 2 == 1:
        raise ValueError("k must be even in this problem setting")

    # 生成测试数据：right 与 down 的边权
    # right: n 行，每行 m-1 条边（但原代码按 m 读取，用 0 填充最后一列）
    # down:  n-1 行，每行 m 条边
    # 为兼容原代码的写法，仍然生成 n x m、(n-1) x m 的矩阵，并让无效位置保持为 0
    max_weight = 10
    right = [[0] * m for _ in range(n)]
    down = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m - 1):  # 最右一列向右没有边，保持为 0
            right[i][j] = random.randint(1, max_weight)
    for i in range(n - 1):
        for j in range(m):
            down[i][j] = random.randint(1, max_weight)

    # 下面是原逻辑改写后版本（去掉所有输入输出封装，直接在内存中计算）
    if k & 1:
        # 原代码在这种情况下打印 -1，但这里直接返回矩阵
        return [[-1] * m for _ in range(n)]

    mem = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            mem[i][j] = 0

    # DP：每次增加 2 步，计算从每个格子出发走 2*k1 步的最小代价的一半
    for _step in range(1, k // 2 + 1):
        mem0 = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                best = float('inf')
                # 上
                if i > 0:
                    best = min(best, mem[i - 1][j] + down[i - 1][j])
                # 下
                if i + 1 < n:
                    best = min(best, mem[i + 1][j] + down[i][j])
                # 左
                if j > 0:
                    best = min(best, mem[i][j - 1] + right[i][j - 1])
                # 右
                if j + 1 < m:
                    best = min(best, mem[i][j + 1] + right[i][j])
                mem0[i][j] = best
        mem = mem0

    # 原代码输出的是 mem[i][j] * 2
    ans = [[mem[i][j] * 2 for j in range(m)] for i in range(n)]
    return ans


if __name__ == "__main__":
    # 示例调用
    n = 5
    result = main(n)
    for row in result:
        print(*row)