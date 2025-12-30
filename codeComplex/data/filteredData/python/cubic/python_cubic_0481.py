import random
import math

M = 998244353
P = 1000000007
Inf = float('inf')


def main(n):
    """
    n: 用作规模参数，这里用于生成网格大小和步数 k 的上界。
       为简单起见，令:
       m = max(1, n // 2)
       k = max(1, n)  (随后会按题意使用 k)
    函数行为:
      1. 随机生成 n x m 的右边边权 rt 以及 (n-1) x m 的下边边权 do
      2. 按原算法计算并打印结果矩阵
    """

    # 根据 n 生成网格尺寸和步数
    m = max(1, n // 2)
    k = max(1, n)

    # 生成测试数据：边权为 1..9 的随机整数
    rt = [[random.randint(1, 9) for _ in range(m - 1)] + [0] for _ in range(n)]
    # 注意：原题中 rt 的尺寸是 n x (m-1)，但原代码使用方式为：
    #   向右: rt[i][j]  (0 <= j < m-1)
    #   向左: rt[i][j-1]
    # 为避免索引越界，这里给每行补一个占位 0 在最后一列，计算时只在合法范围内使用。
    rt = [row[:-1] for row in rt]  # 调整回原始 n x (m-1) 尺寸

    do = [[random.randint(1, 9) for _ in range(m)] for _ in range(n - 1)]

    # 下面是原 solve() 的逻辑，改成直接使用上述生成的数据

    # 若 k 为奇数，全为 -1
    if k % 2 == 1:
        for _ in range(n):
            print(*([-1] * m))
        return

    k //= 2  # 每来回一步视作两步，因此只需做 k/2 次松弛

    dp = [[0] * m for _ in range(n)]
    dp_next = [[P] * m for _ in range(n)]

    for _ in range(k):
        for i in range(n):
            for j in range(m):
                ans = Inf
                # 向上
                if i != 0:
                    ans = min(ans, dp[i - 1][j] + do[i - 1][j])
                # 向左
                if j != 0:
                    ans = min(ans, dp[i][j - 1] + rt[i][j - 1])
                # 向下
                if i != n - 1:
                    ans = min(ans, dp[i + 1][j] + do[i][j])
                # 向右
                if j != m - 1:
                    ans = min(ans, dp[i][j + 1] + rt[i][j])
                dp_next[i][j] = ans

        # 交换 dp 和 dp_next
        for i in range(n):
            for j in range(m):
                dp[i][j] = dp_next[i][j]

    # 输出结果：原代码输出的是 2 * dp[i][j]
    for i in range(n):
        row = []
        for j in range(m):
            row.append(str(2 * dp[i][j]))
        print(" ".join(row))


if __name__ == "__main__":
    # 示例调用，可按需要修改 n
    main(5)