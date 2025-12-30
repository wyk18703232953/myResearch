from math import inf
import random

def main(n):
    # 随机生成参数
    m = n                           # 列数，这里简单设为 n
    K = random.randint(1, 2 * n)    # 步数上限，可根据需要调整规模关系

    # 随机生成边权，范围可按需调整
    max_weight = 10
    hor = [[random.randint(1, max_weight) for _ in range(m - 1)] + [inf] for _ in range(n)]
    vert = [[random.randint(1, max_weight) for _ in range(m)] for _ in range(n - 1)] + [[inf] * m]

    # 如果 K 为奇数，直接输出 -1 表格
    if K % 2:
        for _ in range(n):
            print(*([-1] * m))
        return

    halfK = K // 2
    # dp[k][i][j] = 从 (i,j) 出发，走 2k 步后回到 (i,j) 的最小代价
    dp = [[[inf] * m for _ in range(n)] for _ in range(halfK + 1)]
    dp[0] = [[0] * m for _ in range(n)]

    def valid(i, j):
        return 0 <= i < n and 0 <= j < m

    for k in range(1, halfK + 1):
        for i in range(n):
            for j in range(m):
                # 向右后再回来
                if valid(i, j + 1):
                    dp[k][i][j] = min(dp[k][i][j], dp[k - 1][i][j + 1] + 2 * hor[i][j])
                # 向下后再回来
                if valid(i + 1, j):
                    dp[k][i][j] = min(dp[k][i][j], dp[k - 1][i + 1][j] + 2 * vert[i][j])
                # 向上后再回来
                if valid(i - 1, j):
                    dp[k][i][j] = min(dp[k][i][j], dp[k - 1][i - 1][j] + 2 * vert[i - 1][j])
                # 向左后再回来
                if valid(i, j - 1):
                    dp[k][i][j] = min(dp[k][i][j], dp[k - 1][i][j - 1] + 2 * hor[i][j - 1])

    for row in dp[-1]:
        print(*row)


if __name__ == "__main__":
    # 示例：规模 n = 4，可按需修改或由外部调用 main(n)
    main(4)