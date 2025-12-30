def main(n):
    # 预处理最大值按 n 缩放
    max_val = min(10**7, max(1, n * 10))
    # 预处理平方数
    import math
    limit = int(math.isqrt(max_val)) + 2
    squares = [i * i for i in range(1, limit)]

    # 预处理 p 数组（与原代码一致）
    p = [i for i in range(max_val + 1)]
    for i in range(1, max_val + 1):
        if p[i] == i:
            for sq in squares:
                v = i * sq
                if v > max_val:
                    break
                p[v] = i

    # 根据 n 生成测试数据
    # 构造一次测试：N = n, K = min(20, n)，A 为 1..N 内的随机数
    import random
    random.seed(0)
    N = max(1, n)
    K = min(20, N)  # K 不宜太大以免运算时间过长
    t = 1           # 测试组数

    results = []

    for _ in range(t):
        # 生成 N 个在 [1, max_val] 的随机数
        raw_A = [random.randint(1, max_val) for _ in range(N)]
        A = [p[a] for a in raw_A]

        dp = [N] * (K + 1)
        dp[0] = 1
        used = [set() for _ in range(K + 1)]

        for a in A:
            for j in range(K, -1, -1):
                if dp[j] == N:
                    continue
                if a in used[j]:
                    if j < K and dp[j + 1] > dp[j]:
                        dp[j + 1] = dp[j]
                        used[j + 1] = used[j].copy()
                    dp[j] += 1
                    used[j] = {a}
                else:
                    used[j].add(a)

        results.append(min(dp))

    # 输出结果（与原逻辑的 print 对齐）
    for r in results:
        print(r)


if __name__ == "__main__":
    # 示例：调用 main(1000)
    main(1000)