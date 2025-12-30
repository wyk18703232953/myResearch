from math import inf
import random

mod = 10**9 + 7
mod2 = 998244353

def l1d(n, val=0): 
    return [val for _ in range(n)]

def l2d(n, m, val=0): 
    return [l1d(m, val) for _ in range(n)]

def main(n):
    """
    n 用来控制规模：
    - 网格大小: n x n
    - 步数 k: 取 2*n（保证为偶数，且规模与 n 同级）
    - 边权随机生成 [1, 10]
    """
    # 生成测试数据
    rows = n
    cols = n
    k = 2 * n  # 偶数步数

    # 水平边权: rows x (cols-1)
    hor = [[random.randint(1, 10) for _ in range(cols - 1)] for _ in range(rows)]
    # 垂直边权: (rows-1) x cols
    ver = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows - 1)]

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
    # 示例：调用 main(5) 生成 5x5 网格的测试并输出结果
    main(5)