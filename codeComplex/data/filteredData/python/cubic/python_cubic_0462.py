import random

def main(n: int):
    # 生成测试数据
    # 规模 n 控制网格大小，这里令 m = n，k = 2*n 作为示例
    m = n
    k = 2 * n  # 偶数，避免全 -1 的情况；可按需调整

    # 生成权值矩阵，模拟原始 left 和 down
    # left: n 行, m-1 列；down: n-1 行, m 列
    MAX_W = 10**3
    left = [[random.randint(1, MAX_W) for _ in range(m - 1)] for _ in range(n)]
    down = [[random.randint(1, MAX_W) for _ in range(m)] for _ in range(n - 1)]

    inf = 1 << 60

    if k & 1:
        for _ in range(n):
            print(*[-1] * m)
        return

    ans = [[0] * m for _ in range(n)]
    steps = k // 2
    for _ in range(1, steps + 1):
        dp_next = [[inf] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i > 0:
                    dp_next[i][j] = min(dp_next[i][j], ans[i - 1][j] + down[i - 1][j])
                if i < n - 1:
                    dp_next[i][j] = min(dp_next[i][j], ans[i + 1][j] + down[i][j])
                if j > 0:
                    dp_next[i][j] = min(dp_next[i][j], ans[i][j - 1] + left[i][j - 1])
                if j < m - 1:
                    dp_next[i][j] = min(dp_next[i][j], ans[i][j + 1] + left[i][j])
        ans = dp_next

    for i in range(n):
        for j in range(m):
            print(ans[i][j] * 2, end=' ')
        print()


if __name__ == "__main__":
    # 示例：n = 4
    main(4)