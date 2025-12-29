def main(n):
    # 预处理：平方因子压缩（与原程序逻辑相同）
    squares = [i * i for i in range(1, 3162)]

    p = list(range(n + 1))
    for i in range(1, n + 1):
        if p[i] == i:
            for sq in squares:
                if i * sq > n:
                    break
                p[i * sq] = i

    # -------- 生成测试数据部分 ----------
    # 生成一个测试：T 组数据
    # 每组数据为 (N, K, A)
    # 为了演示，这里构造：
    # T = 3
    # 1) 小规模
    # 2) 中规模
    # 3) 尽量接近 n 范围内的随机测试
    import random

    random.seed(0)

    tests = []

    # 1) 小规模
    N1 = min(10, n)
    K1 = 2
    A1 = [random.randint(1, n) for _ in range(N1)]
    tests.append((N1, K1, A1))

    # 2) 中规模
    N2 = min(1000, n)
    K2 = min(10, N2 // 2 + 1)
    A2 = [random.randint(1, n) for _ in range(N2)]
    tests.append((N2, K2, A2))

    # 3) 较大规模（受 n 限制）
    N3 = min(100000, n)
    K3 = min(20, N3 // 2 + 1)
    A3 = [random.randint(1, n) for _ in range(N3)]
    tests.append((N3, K3, A3))

    T = len(tests)

    # -------- 原核心逻辑（去除 input） ----------
    results = []
    for idx in range(T):
        N, K, A_raw = tests[idx]
        A = [p[a] for a in A_raw]

        dp = [N] * (K + 1)
        dp[0] = 1
        # 注意：原代码 used = [{}] * (K + 1) 会导致所有元素引用同一字典
        # 这里保留原逻辑（包括这一点），以忠实还原行为
        used = [{}] * (K + 1)

        for a in A:
            for j in range(K, -1, -1):
                if dp[j] == N:
                    continue
                if a in used[j]:
                    if j < K and dp[j + 1] > dp[j]:
                        dp[j + 1] = dp[j]
                        used[j + 1] = used[j]
                    dp[j] += 1
                    used[j] = {}
                used[j][a] = 1
        results.append(min(dp))

    # 输出结果（原代码是 print，每个测试一行）
    for ans in results:
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模上限设为 10**5（避免演示时过慢）
    main(10**5)