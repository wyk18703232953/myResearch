import random

def main(n):
    # 这里将原来的 (n, m, k) 统一成规模参数 n：
    # 为了演示，令 m = n, k = 2 * n（可按需要修改生成规则）
    m = n
    k = 2 * n

    # 生成测试数据：dist1 为 n 行 m-1 列，dist2 为 n-1 行 m 列
    # 原代码使用 dist1[i][j] 作为 (i,j) <-> (i,j+1) 的边权
    # dist2[i][j] 作为 (i,j) <-> (i+1,j) 的边权
    # 这里用 1~10 的随机正整数
    random.seed(0)
    dist1 = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    dist2 = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    if k % 2:
        print(' '.join(map(str, [-1] * (n * m))))
        return

    k //= 2
    INF = 10 ** 9
    dp = [INF] * ((k + 1) * n * m)

    # t = 0 层初始化
    for i in range(n):
        for j in range(m):
            dp[i * m + j] = 0

    for t in range(k):
        r = (t + 1) * n * m
        q = t * n * m
        for i in range(n):
            base_q = q + i * m
            base_r = r + i * m
            # 内层对 j 循环时少做一次乘法以稍微优化
            for j in range(m):
                cur = base_q + j
                cur_val = dp[cur]
                if cur_val == INF:
                    continue
                # 向下
                if i < n - 1:
                    nxt = r + (i + 1) * m + j
                    cost = cur_val + 2 * dist2[i][j]
                    if cost < dp[nxt]:
                        dp[nxt] = cost
                # 向上
                if i > 0:
                    nxt = r + (i - 1) * m + j
                    cost = cur_val + 2 * dist2[i - 1][j]
                    if cost < dp[nxt]:
                        dp[nxt] = cost
                # 向右
                if j < m - 1:
                    nxt = base_r + j + 1
                    cost = cur_val + 2 * dist1[i][j]
                    if cost < dp[nxt]:
                        dp[nxt] = cost
                # 向左
                if j > 0:
                    nxt = base_r + j - 1
                    cost = cur_val + 2 * dist1[i][j - 1]
                    if cost < dp[nxt]:
                        dp[nxt] = cost

    ans = []
    last_layer_offset = k * n * m
    for i in range(n):
        base = last_layer_offset + i * m
        for j in range(m):
            ans.append(dp[base + j])

    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    # 示例调用：规模 n=4
    main(4)