from collections import defaultdict
import random

def main(n):
    # 生成测试数据
    # 这里设置 m 与 n 相同，k 为一个偶数（例如 4），
    # 若需要可自行调整生成逻辑
    m = n
    k = 4  # 必须为偶数才有意义，原代码中若 k 为奇数则全为 -1

    # 生成权重矩阵 a: n 行 m-1 列（每行横向边权）
    a = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    # 生成权重矩阵 b: n-1 行 m 列（每行纵向边权）
    b = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    if k % 2:
        ans = [-1] * m
        for _ in range(n):
            print(*ans)
        return

    G = [[] for _ in range(n * m + 1)]
    for i in range(n):
        a0 = a[i]
        for j in range(m - 1):
            x = a0[j]
            G[i * m + j].append((i * m + j + 1, x))
            G[i * m + j + 1].append((i * m + j, x))

    for i in range(n - 1):
        b0 = b[i]
        for j in range(m):
            x = b0[j]
            G[i * m + j].append(((i + 1) * m + j, x))
            G[(i + 1) * m + j].append((i * m + j, x))

    dp = [0] * (n * m)
    dp0 = [0] * (n * m)
    inf = 1145141919

    for i in range(n):
        for j in range(m):
            s = i * m + j
            dps = inf
            for t, x in G[s]:
                dps = min(dps, 2 * x)
            dp[s] = dps
            dp0[s] = dps

    for _ in range((k - 2) // 2):
        dp1 = [0] * (n * m)
        for i in range(n):
            for j in range(m):
                s = i * m + j
                dps = dp0[s] + 2 * dp[s]
                for t, x in G[s]:
                    dps = min(dps, 2 * x + dp0[t])
                dp1[s] = dps
        dp0 = dp1

    for i in range(n):
        ans = dp0[(m * i):(m * (i + 1))]
        print(*ans)


if __name__ == "__main__":
    # 示例调用：n = 4
    main(4)