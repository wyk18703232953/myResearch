def main(n):
    """
    n 为规模参数，用于生成测试数据：
      - 生成 t=1 组数据
      - 对该组数据：k = n // 2（至少为 1）
      - zc 为长度为 n 的数组，每个元素在 [1, 10^7] 范围内
    """
    import random

    MAXV = 10_000_000

    # 预处理 p[i]：记录 i 的最小质因子（p[i] = i 表示 i 为质数）
    pfs = [i * i for i in range(1, 3163)]
    p = [i for i in range(0, MAXV + 1)]
    for i in range(2, MAXV + 1):
        if p[i] == i:  # i 是质数
            for j in pfs:
                v = i * j
                if v > MAXV:
                    break
                p[v] = i

    # 生成测试数据
    t = 1
    # n 为数组长度
    k = max(1, n // 2)
    # 生成 n 个 [1, MAXV] 之间的随机整数
    zc = [random.randint(1, MAXV) for _ in range(n)]

    # 将原逻辑封装为对一组数据的处理函数
    def solve_case(n, k, zc):
        s = [p[x] for x in zc]  # 每个数取其最小质因子
        dp = [n] * (k + 1)
        dp[0] = 1
        ys = [{} for _ in range(k + 1)]

        for val in s:
            for j in range(k, -1, -1):
                if dp[j] == n:
                    continue
                if val in ys[j]:
                    if j < k and dp[j] < dp[j + 1]:
                        dp[j + 1] = dp[j]
                        ys[j + 1] = ys[j].copy()
                    dp[j] += 1
                    ys[j].clear()
                ys[j][val] = 1
        return min(dp)

    # 这里 t 固定为 1，仅演示多组数据时的循环结构
    for _ in range(t):
        ans = solve_case(n, k, zc)
        print(ans)


if __name__ == "__main__":
    # 示例：规模为 100
    main(100)