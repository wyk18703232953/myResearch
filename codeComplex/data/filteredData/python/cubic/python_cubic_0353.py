def main(n):
    # 预处理：平方因子压缩
    squares = [i * i for i in range(1, int(n**0.5) + 2)]
    p = list(range(n + 1))
    for i in range(1, n + 1):
        if p[i] == i:
            for sq in squares:
                v = i * sq
                if v > n:
                    break
                p[v] = i

    # -------- 生成测试数据部分 --------
    # 可按需要修改生成规则

    # 测试组数 T
    T = 3

    # 为每组构造 (N, K, A)
    # 这里示例生成：N 递增，K 适中，A 为 1..N 中的随机选取（直接用前 N 个数示意）
    import math
    tests = []
    for t in range(T):
        # N 尽量不要太大，否则 DP 会非常耗时；这里与 n 关联做示例
        N = min(2000 + 1000 * t, n)
        K = min(20 + t, N)  # K 不超过 N
        # 生成数组 A（长度 N），元素在 [1, n] 范围内
        # 这里简单用 1..N 截断到 n
        A = [i if i <= n else n for i in range(1, N + 1)]
        tests.append((N, K, A))
    # ---------------------------------

    # 主逻辑（用生成好的 tests 替代原先的输入）
    res = []
    for (N, K, A_raw) in tests:
        A = [p[a] for a in A_raw]  # 映射到平方因子压缩后的值
        dp = [N] * (K + 1)
        dp[0] = 1
        used = [{} for _ in range(K + 1)]
        for a in A:
            for j in range(K, -1, -1):
                if dp[j] == N:
                    continue
                if a in used[j]:
                    if j < K and dp[j + 1] > dp[j]:
                        dp[j + 1] = dp[j]
                        used[j + 1] = used[j].copy()
                    dp[j] += 1
                    used[j] = {}
                used[j][a] = 1
        res.append(min(dp))

    # 输出结果（模拟原来的 print）
    for v in res:
        print(v)


if __name__ == "__main__":
    # 这里给一个默认规模示例，可以按需要修改
    main(10**5)