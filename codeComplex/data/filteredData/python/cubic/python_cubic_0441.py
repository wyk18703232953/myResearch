from math import inf
import random

mod = 10 ** 9 + 7
mod2 = 998244353

def l1d(n, val=0):
    return [val for _ in range(n)]

def l2d(n, m, val=0):
    return [l1d(m, val) for _ in range(n)]

def main(n):
    """
    n: 控制规模的参数，用来生成测试数据。
       这里约定：
       - 网格行数 rows = n
       - 网格列数 cols = max(1, n)（至少为1）
       - k = 2 * n（保证是偶数，方便算法运行）
       权重随机生成在 [1, 10] 内。
    """
    rows = n
    cols = max(1, n)
    k = 2 * n  # 偶数

    # 生成测试数据：hor 为每行的横向边权，大小 rows x (cols-1)
    # ver 为每行之间的纵向边权，大小 (rows-1) x cols
    rng = random.Random(2025)

    hor = []
    for _ in range(rows):
        if cols - 1 > 0:
            hor.append([rng.randint(1, 10) for _ in range(cols - 1)])
        else:
            hor.append([])

    ver = []
    for _ in range(rows - 1):
        ver.append([rng.randint(1, 10) for _ in range(cols)])

    # 原逻辑开始
    if k % 2:
        ml = l2d(rows, cols, -1)
        for row in ml:
            print(*row)
        return

    k //= 2
    dp = [l2d(rows, cols) for _ in range(k + 1)]
    for f in range(1, k + 1):
        for i in range(rows):
            for j in range(cols):
                a = inf
                if i != 0:
                    a = min(a, 2 * ver[i - 1][j] + dp[f - 1][i - 1][j])
                if i != rows - 1:
                    a = min(a, 2 * ver[i][j] + dp[f - 1][i + 1][j])
                if j != 0:
                    a = min(a, 2 * hor[i][j - 1] + dp[f - 1][i][j - 1])
                if j != cols - 1:
                    a = min(a, 2 * hor[i][j] + dp[f - 1][i][j + 1])
                dp[f][i][j] = a

    for row in dp[-1]:
        print(*row)


if __name__ == "__main__":
    # 示例：可以修改这里的 n 来改变规模
    main(3)