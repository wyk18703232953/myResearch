#!/usr/bin/env python
import random

def main(n):
    """
    n: 规模参数，用于生成测试数据的大小。
       在原题中有 n, m, k 三个参数，这里统一用 n 派生：
       - 行数 rows = n
       - 列数 cols = max(1, n)  （保证至少 1 列）
       - 步数 k = 2 * n         （保证为偶数，使结果不是全 -1）
    """
    # 根据 n 生成测试数据
    rows = n
    cols = max(1, n)
    k = 2 * n  # 保证为偶数

    # 如果 k 为奇数，按原逻辑输出 -1 矩阵
    if k % 2:
        ans = [[-1] * cols for _ in range(rows)]
        for li in ans:
            print(*li)
        return

    # 生成水平边权 crr: rows x (cols-1)
    # 对应原代码中第一批输入
    crr = []
    for _ in range(rows):
        if cols <= 1:
            crr.append([])
        else:
            row = [random.randint(1, 10) for _ in range(cols - 1)]
            crr.append(row)

    # 生成垂直边权 rrr: (rows-1) x cols
    # 对应原代码中第二批输入
    rrr = []
    for _ in range(rows - 1):
        row = [random.randint(1, 10) for _ in range(cols)]
        rrr.append(row)

    # 初始化 dp
    dp = [[float('inf')] * cols for _ in range(rows)]

    # 用边权初始化 dp（与原代码相同逻辑）
    for i in range(rows):
        arr = crr[i]
        for j in range(cols - 1):
            dp[i][j] = min(dp[i][j], arr[j])
            dp[i][j + 1] = min(dp[i][j + 1], arr[j])

    for i in range(rows - 1):
        arr = rrr[i]
        for j in range(cols):
            dp[i][j] = min(dp[i][j], arr[j])
            dp[i + 1][j] = min(dp[i + 1][j], arr[j])

    # 动态规划扩展 k//2 - 1 次
    for _ in range(1, k // 2):
        ndp = [[float('inf')] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                x, y = i, j
                if x > 0:
                    ndp[i][j] = min(ndp[i][j], dp[x - 1][y] + rrr[x - 1][y])
                if x < rows - 1:
                    ndp[i][j] = min(ndp[i][j], dp[x + 1][y] + rrr[x][y])
                if y > 0:
                    ndp[i][j] = min(ndp[i][j], dp[x][y - 1] + crr[x][y - 1])
                if y < cols - 1:
                    ndp[i][j] = min(ndp[i][j], dp[x][y + 1] + crr[x][y])
        dp = ndp

    # 输出答案（乘以 2）
    for li in dp:
        li = [2 * x for x in li]
        print(*li)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(3)