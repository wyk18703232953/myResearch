from collections import defaultdict
from sys import stdout


def main(n):
    """
    将原始基于输入的程序改为可参数化的版本。
    参数：
        n: 网格规模基数，这里构造 n x n 网格，步数 K = 2 * n。
    """
    # 生成测试数据：n x n 网格，K = 2*n（保证为偶数）
    m = n           # 列数
    K = 2 * n       # 总步数，保证为偶数且与规模相关

    # 生成边权：
    # l1[i][j] 表示 (i,j) -> (i,j+1) 和 (i,j+1) -> (i,j) 的边权
    # l2[i][j] 表示 (i,j) -> (i+1,j) 和 (i+1,j) -> (i,j) 的边权
    # 这里用简单的可重复测试数据：常数或线性权重，也可以改成随机。
    l1 = [[1 for _ in range(m - 1)] for _ in range(n)]         # 水平边权
    l2 = [[1 for _ in range(m)] for _ in range(n - 1)]         # 竖直边权

    # 若 K 为奇数，全为 -1；这里 K = 2*n 一定是偶数，但保持逻辑完整
    if K % 2:
        for i in range(n):
            for j in range(m):
                stdout.write('-1 ')
            stdout.write('\n')
        return

    # dp[i][j][h]：从 (i,j) 出发恰好走 h 步回到某一点（不要求回起点）的最小距离的一半逻辑
    # 实际原题含义：走 K 步回到同一格子的最小总权，使用 K/2 步 DP 再乘 2
    max_half = K // 2
    INF = 10 ** 9

    # 初始化 dp 数组：大小 n x m x (max_half+1)
    dp = [[[0] * (max_half + 1) for _ in range(m)] for _ in range(n)]

    # 逐步扩展步数
    for k in range(1, max_half + 1):
        for i in range(n):
            for j in range(m):
                res = INF
                # 上
                if i - 1 >= 0:
                    res = min(res, l2[i - 1][j] + dp[i - 1][j][k - 1])
                # 下
                if i + 1 < n:
                    res = min(res, l2[i][j] + dp[i + 1][j][k - 1])
                # 右
                if j + 1 < m:
                    res = min(res, l1[i][j] + dp[i][j + 1][k - 1])
                # 左
                if j - 1 >= 0:
                    res = min(res, l1[i][j - 1] + dp[i][j - 1][k - 1])

                dp[i][j][k] = res

    # 输出答案：每个格子走 K 步回到自身的最小代价
    for i in range(n):
        for j in range(m):
            stdout.write(str(2 * dp[i][j][max_half]) + ' ')
        stdout.write('\n')


if __name__ == "__main__":
    # 示例：调用 main(3) 生成 3x3 网格测试
    main(3)