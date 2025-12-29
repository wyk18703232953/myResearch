# coding:utf-8
# @Author: 将立（改写去除 input，封装为 main(n)）

import random

def main(n):
    """
    n: 规模参数，用于生成测试数据。
       本例中将 n 视为网格行数，列数 m 与 n 相同（可按需修改）。
    """
    # 可根据需要调整 m 与 K 的生成方式
    m = n                      # 列数，这里简单设为与 n 相同
    # 保证 K 为偶数，且不超过 2*10 以适配 f 的第三维大小 11
    K = min(2 * ((n + 1) // 2), 20)
    if K % 2 == 1:
        K += 1
    K = max(2, K)              # 至少为 2，且为偶数

    # 生成测试数据：边权重随机 [1, 9]
    wh = [[0] * m for _ in range(n)]  # 水平边权：行 i，列 j -> (i, j+1)
    wv = [[0] * m for _ in range(n)]  # 垂直边权：行 i，列 j -> (i+1, j)

    for i in range(n):
        for j in range(m - 1):
            wh[i][j] = random.randint(1, 9)

    for i in range(n - 1):
        for j in range(m):
            wv[i][j] = random.randint(1, 9)

    INF = int(1e8)
    # 第三维最多使用到 K//2，且 K//2 <= 10（由上面对 K 的限制保证）
    max_k = min(K // 2, 10)
    f = [[[INF] * 11 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            f[i][j][0] = 0

    for k in range(1, max_k + 1):
        for i in range(n):
            for j in range(m):
                if i > 0:
                    f[i][j][k] = min(f[i][j][k], f[i - 1][j][k - 1] + wv[i - 1][j])
                if j < m - 1:
                    f[i][j][k] = min(f[i][j][k], f[i][j + 1][k - 1] + wh[i][j])
                if i < n - 1:
                    f[i][j][k] = min(f[i][j][k], f[i + 1][j][k - 1] + wv[i][j])
                if j > 0:
                    f[i][j][k] = min(f[i][j][k], f[i][j - 1][k - 1] + wh[i][j - 1])

    for i in range(n):
        row_ans = []
        for j in range(m):
            if K % 2 == 1:
                row_ans.append("-1")
            else:
                half = K // 2
                half = min(half, 10)  # 与 f 的第三维对齐
                dp = [INF] * (half + 1)
                dp[0] = 0
                for k in range(1, half + 1):
                    for l in range(0, k):
                        dp[k] = min(dp[k], dp[l] + f[i][j][k - l] * 2)
                row_ans.append(str(dp[half]))
        print(" ".join(row_ans))


if __name__ == "__main__":
    # 示例调用：n = 5
    main(5)