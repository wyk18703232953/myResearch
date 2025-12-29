import random

def main(n):
    # 规模说明：
    #   网格大小：n 行，m 列（此处令 m = n）
    #   k：总步数（必须为偶数，算法中会除以 2）
    #
    # 随机生成：
    #   hozs: n 行, m-1 列，水平方向边权
    #   verts: n-1 行, m 列，垂直方向边权

    high = 10 ** 12
    m = n
    # 令总步数随规模增长，这里选一个典型值（可按需修改）
    total_k = 2 * max(1, n // 2)  # 保证为偶数且 >= 2

    k = total_k
    # 生成随机边权，范围 [1, 10]
    hozs = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    verts = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    if k % 2:
        for _ in range(n):
            print("-1 " * m)
        return

    k //= 2

    # 初始化 dp[i][j][depth]
    dp = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

    for depth in range(1, k + 1):
        for i in range(n):
            for j in range(m):
                if i == 0:
                    up = high
                else:
                    up = verts[i - 1][j] + dp[i - 1][j][depth - 1]
                if i == n - 1:
                    down = high
                else:
                    down = verts[i][j] + dp[i + 1][j][depth - 1]
                if j == 0:
                    left = high
                else:
                    left = hozs[i][j - 1] + dp[i][j - 1][depth - 1]
                if j == m - 1:
                    right = high
                else:
                    right = hozs[i][j] + dp[i][j + 1][depth - 1]

                min_cost = min(up, down, left, right)
                dp[i][j][depth] = dp[i][j][depth] + min_cost

    for i in range(n):
        print(*[2 * dp[i][j][k] for j in range(m)])


if __name__ == "__main__":
    # 示例调用：规模 n = 4
    main(4)