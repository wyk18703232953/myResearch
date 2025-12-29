def main(n):
    import random

    # 1) 生成规模参数
    # 将原来的 (n, m, k) 都用 main 的参数 n 来控制
    # 这里设：
    #   行数 rows = n
    #   列数 cols = n
    #   步数 k 取为一个不太大的偶数（例如 <= 20），避免 DP 维度过大
    rows = n
    cols = n
    # 保证 k 为偶数，且不超过 20
    k = min(2 * ((n % 10) + 1), 20)
    if k % 2 == 1:
        k += 1

    # 2) 根据 n 生成测试数据 l1, l2
    # l1: rows x cols 的网格，左右边的代价
    # l2: (rows-1) x cols 的网格，上下边的代价
    # 代价随机在 1~9 之间
    l1 = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
    if rows > 1:
        l2 = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows - 1)]
    else:
        l2 = []

    # 3) 核心逻辑（移除所有 input，直接使用上面生成的数据）
    def check(x, y):
        return 0 <= x < rows and 0 <= y < cols

    inf = 10 ** 18
    # dp[i][j][t]: 从 (i,j) 出发，走恰好 t 步到任意点的最小代价的一半路径（原题思路）
    max_half = k // 2
    dp = [[[inf] * (max_half + 1) for _ in range(cols)] for __ in range(rows)]

    # t = 1 初始化
    for i in range(rows):
        for j in range(cols):
            if check(i, j + 1):
                dp[i][j][1] = min(l1[i][j], dp[i][j][1])
            if check(i, j - 1):
                dp[i][j][1] = min(l1[i][j - 1], dp[i][j][1])
            if check(i + 1, j) and rows > 1:
                dp[i][j][1] = min(l2[i][j], dp[i][j][1])
            if check(i - 1, j) and rows > 1:
                dp[i][j][1] = min(l2[i - 1][j], dp[i][j][1])

    # t = 2..k//2
    for t in range(2, max_half + 1):
        for i in range(rows):
            for j in range(cols):
                if check(i, j + 1):
                    dp[i][j][t] = min(dp[i][j][t], l1[i][j] + dp[i][j + 1][t - 1])
                if check(i, j - 1):
                    dp[i][j][t] = min(dp[i][j][t], l1[i][j - 1] + dp[i][j - 1][t - 1])
                if check(i + 1, j) and rows > 1:
                    dp[i][j][t] = min(dp[i][j][t], l2[i][j] + dp[i + 1][j][t - 1])
                if check(i - 1, j) and rows > 1:
                    dp[i][j][t] = min(dp[i][j][t], l2[i - 1][j] + dp[i - 1][j][t - 1])

    # 4) 计算答案
    ans = [[inf] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if k % 2:
                ans[i][j] = -1
            else:
                ans[i][j] = 2 * dp[i][j][max_half]

    # 5) 输出（只保留核心输出）
    for row in ans:
        print(*row)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)