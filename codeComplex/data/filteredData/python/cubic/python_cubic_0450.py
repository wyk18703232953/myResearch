import random

def main(n):
    # 规模参数：n 为行数，列数 m、步数 k 可按需要设定或派生
    m = n               # 这里简单设为方阵，可根据需要修改
    k = 2 * n           # 保证为偶数步，可根据需要修改

    # 生成测试数据：left 为 n x (m-1)，right 为 (n-1) x m 的非负权值
    left = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    right = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    dp_old = [[0 for _ in range(m)] for _ in range(n)]

    if k % 2 != 0:
        for _ in range(n):
            print(*[-1 for _ in range(m)])
        return

    k //= 2
    for _ in range(k):
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for row in range(n):
            for col in range(m):
                t = float("inf")
                if col > 0:
                    t = min(t, dp_old[row][col - 1] + 2 * left[row][col - 1])
                if col < m - 1:
                    t = min(t, dp_old[row][col + 1] + 2 * left[row][col])
                if row > 0:
                    t = min(t, dp_old[row - 1][col] + 2 * right[row - 1][col])
                if row < n - 1:
                    t = min(t, dp_old[row + 1][col] + 2 * right[row][col])
                dp[row][col] = t
        dp_old = dp

    for i in range(n):
        print(*dp_old[i])


if __name__ == "__main__":
    # 示例调用：n=4
    main(4)