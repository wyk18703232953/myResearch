import random

def main(n):
    # 生成测试数据：n 行 n 列，k 为偶数步长
    m = n
    # 让 k 与 n 同级，保证是偶数，且至少为 2
    k = max(2, (2 * ((n + 1) // 2)))

    # 生成随机边权，范围可自行调整
    # 横向边：n 行，每行 m-1 个
    horizontal = [
        [random.randint(1, 10) for _ in range(m - 1)]
        for _ in range(n)
    ]
    # 纵向边：n-1 行，每行 m 个
    vertical = [
        [random.randint(1, 10) for _ in range(m)]
        for _ in range(n - 1)
    ]

    if k % 2 == 1:
        for _ in range(n):
            print(" ".join(["-1"] * m))
        return

    kk = k
    # maps[i][j][d] : 从 (i,j) 出发，方向 d 的边权
    # d = 0: 右, 1: 左, 2: 下, 3: 上
    maps = [[[0 for _ in range(4)] for _ in range(m)] for _ in range(n)]

    # 初始化 DP
    INF = 10**18
    dp = [[[INF for _ in range(k // 2 + 1)] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0

    # 填充横向边
    for i in range(n):
        s = horizontal[i]
        for j in range(m - 1):
            maps[i][j][0] = s[j]       # 右
            maps[i][j + 1][1] = s[j]   # 左

    # 填充纵向边
    for i in range(n - 1):
        s = vertical[i]
        for j in range(m):
            maps[i][j][2] = s[j]       # 下
            maps[i + 1][j][3] = s[j]   # 上

    # 动态规划
    for step in range(1, kk // 2 + 1):
        for i in range(n):
            for j in range(m):
                cur = dp[i][j][step - 1]
                if cur == INF:
                    continue
                if j < m - 1:
                    dp[i][j + 1][step] = min(dp[i][j + 1][step], cur + maps[i][j][0])
                if i < n - 1:
                    dp[i + 1][j][step] = min(dp[i + 1][j][step], cur + maps[i][j][2])
                if i > 0:
                    dp[i - 1][j][step] = min(dp[i - 1][j][step], cur + maps[i][j][3])
                if j > 0:
                    dp[i][j - 1][step] = min(dp[i][j - 1][step], cur + maps[i][j][1])

    final_step = kk // 2
    for i in range(n):
        row = []
        for j in range(m):
            row.append(str(dp[i][j][final_step] * 2))
        print(" ".join(row))


if __name__ == "__main__":
    # 示例：调用 main(4)
    main(4)