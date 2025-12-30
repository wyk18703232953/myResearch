import random

# 预处理：最小质因子或本题所需的“平方因子”化简
MAXV = 10_000_000

pfs = [i * i for i in range(1, 3163)]
p = [i for i in range(0, MAXV + 1)]
for i in range(1, MAXV + 1):
    if p[i] == i:
        for j in pfs:
            v = i * j
            if v > MAXV:
                break
            p[v] = i


def main(n):
    """
    n: 规模参数，用于生成随机测试数据。
       我们令：
       - t = 1（测试组数）
       - k = max(1, n // 5)
       - 数组 zc 长度 = n
       - zc[i] 在 [1, MAXV] 内随机
    """
    random.seed(1)

    t = 1
    for _ in range(t):
        k = max(1, n // 5)
        zc = [random.randint(1, MAXV) for _ in range(n)]

        s = [p[x] for x in zc]
        dp = [n] * (k + 1)
        dp[0] = 1
        ys = [{} for _ in range(n + 1)]

        for val in s:
            for j in range(k, -1, -1):
                if dp[j] == n:
                    continue
                if ys[j].get(val, -1) != -1:
                    if j < k and dp[j] < dp[j + 1]:
                        dp[j + 1] = dp[j]
                        ys[j + 1] = ys[j].copy()
                    dp[j] += 1
                    ys[j] = {}
                ys[j][val] = 1

        print(min(dp))


if __name__ == "__main__":
    # 示例：调用 main(1000)
    main(1000)