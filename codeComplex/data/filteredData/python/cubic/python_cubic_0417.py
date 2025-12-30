import random

INF = 10**20 + 1

def main(n):
    # 生成规模：n 行，m 列，k 为偶数步数
    m = n
    k = 2 * n  # 任意偶数，和规模相关即可

    # 生成测试数据：边权取 [1, 10] 的随机整数
    hor = [[random.randint(1, 10) for _ in range(m - 1)] + [INF] for _ in range(n)]
    ver = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)] + [[INF] * m]

    if k & 1:
        for _ in range(n):
            print(*[-1] * m)
        return

    dp = [[0] * m for _ in range(n)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    for _ in range(k // 2):
        dp1 = [[INF] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                for kk in range(4):
                    x1, y1 = i + dx[kk], j + dy[kk]
                    if not (0 <= x1 < n and 0 <= y1 < m):
                        continue
                    if kk < 2:
                        ed = hor[i][j - (kk == 1)]
                    else:
                        ed = ver[i - (kk == 3)][j]
                    if ed != INF:
                        dp1[i][j] = min(dp1[i][j], 2 * ed + dp[x1][y1])
        dp = dp1

    for row in dp:
        print(*row)


if __name__ == "__main__":
    # 示例调用：规模 n=4
    main(4)