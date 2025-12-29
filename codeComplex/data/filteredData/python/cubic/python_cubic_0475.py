import random

def main(n):
    # 生成规模参数
    # 这里令 m 与 n 相同，k 为一个不超过 2*(n+m) 的偶数（保证有意义）
    m = n
    # 随机生成偶数步数 k（至少为 2）
    max_k = max(2, 2 * (n + m))
    k = random.randrange(2, max_k + 1, 2)  # 随机偶数

    # 生成测试数据：
    # lr: n 行 m-1 列，ud: n-1 行 m 列，权值为 1~10 之间的随机正整数
    lr = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    ud = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    # 如果 k 为奇数，输出 -1（本题逻辑），不过我们已经设定 k 为偶数
    if k % 2:
        arr = [-1] * m
        for _ in range(n):
            print(*arr)
        return

    kk = k // 2
    INF = 10 ** 10

    # dp[i][j][z]: 从 (i,j) 出发，走 z 步到达某点的最小花费
    dp = [[[INF] * (kk + 1) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0

    for z in range(1, kk + 1):
        for i in range(n):
            for j in range(m):
                cur = dp[i][j][z]
                # 上
                if i > 0:
                    cand = dp[i - 1][j][z - 1] + ud[i - 1][j]
                    if cand < cur:
                        cur = cand
                # 下
                if i < n - 1:
                    cand = dp[i + 1][j][z - 1] + ud[i][j]
                    if cand < cur:
                        cur = cand
                # 左
                if j > 0:
                    cand = dp[i][j - 1][z - 1] + lr[i][j - 1]
                    if cand < cur:
                        cur = cand
                # 右
                if j < m - 1:
                    cand = dp[i][j + 1][z - 1] + lr[i][j]
                    if cand < cur:
                        cur = cand
                dp[i][j][z] = cur

    ans = [[dp[i][j][kk] * 2 for j in range(m)] for i in range(n)]
    for i in range(n):
        print(*ans[i])


if __name__ == "__main__":
    # 示例调用：n = 4
    main(4)