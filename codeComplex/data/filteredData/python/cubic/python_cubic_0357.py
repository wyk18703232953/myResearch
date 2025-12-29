pfs = [i * i for i in range(1, 3163)]
MAXV = 10_000_000

# 预处理 p 数组：p[x] = x 的最小素因子平方式分解后剩下的平方因子（原逻辑）
p = [i for i in range(0, MAXV + 1)]
for i in range(1, MAXV + 1):
    if p[i] == i:
        for j in pfs:
            if i * j > MAXV:
                break
            p[i * j] = i


def main(n):
    """
    n 为规模参数：
    - 构造一组测试数据 (单组测试)
    - 数组长度设为 n，元素值在 [1, 10^7] 内
    - k 设置为 n // 3（至少为 1）
    """
    import random

    # 生成 1 组测试数据，模仿原程序的单组行为
    t = 1
    for _ in range(t):
        k = max(1, n // 3)
        # 为了让预处理有效，随机数范围限制在 [1, MAXV]
        zc = [random.randint(1, MAXV) for _ in range(n)]

        # 核心逻辑与原代码一致
        s = [p[zc[i]] for i in range(len(zc))]
        dp = [n] * (k + 1)
        dp[0] = 1
        ys = [{} for _ in range(n + 1)]

        for i in range(len(s)):
            for j in range(k, -1, -1):
                if dp[j] == n:
                    continue
                if ys[j].get(s[i], -1) != -1:
                    if j < k and dp[j] < dp[j + 1]:
                        dp[j + 1] = dp[j]
                        ys[j + 1] = ys[j]
                    dp[j] += 1
                    ys[j] = {}
                ys[j][s[i]] = 1

        print(min(dp))


# 示例：直接运行文件时，给一个默认规模
if __name__ == "__main__":
    main(10)