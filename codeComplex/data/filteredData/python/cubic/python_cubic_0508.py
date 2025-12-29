import random

INF = 10**20


def main(n):
    # 生成规模为 n 的测试数据
    # 这里设定 m = n，k = 2 * n 作为示例，可按需调整
    m = n
    k = 2 * n

    # 生成边权：1~10 的随机整数
    ea = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]      # 水平边
    eb = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]      # 垂直边

    # DP 数组初始化
    dp = [[[INF] * m for __ in range(n)] for _ in range(k // 2 + 1)]
    dp[0] = [[0] * m for _ in range(n)]

    def show_ans():
        for line in dp[-1]:
            print(' '.join(map(str, [d * 2 for d in line])))

    # 若 k 为奇数，答案必为 -1
    if k % 2:
        for _ in range(n):
            print(' '.join(['-1'] * m))
        return

    # 状态转移
    for t in range(1, k // 2 + 1):
        for i in range(n):
            for j in range(m):
                cur = dp[t][i][j]
                if i > 0:
                    cost = dp[t - 1][i - 1][j] + eb[i - 1][j]
                    if cost < cur:
                        cur = cost
                if i < n - 1:
                    cost = dp[t - 1][i + 1][j] + eb[i][j]
                    if cost < cur:
                        cur = cost
                if j > 0:
                    cost = dp[t - 1][i][j - 1] + ea[i][j - 1]
                    if cost < cur:
                        cur = cost
                if j < m - 1:
                    cost = dp[t - 1][i][j + 1] + ea[i][j]
                    if cost < cur:
                        cur = cost
                dp[t][i][j] = cur

    show_ans()


if __name__ == "__main__":
    # 示例运行：n = 5
    main(5)