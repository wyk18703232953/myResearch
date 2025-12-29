def main(n):
    # n 作为规模参数，用来生成测试数据
    # 这里约定：生成 t = 1 组测试，每组：
    # N = n，K = min(20, max(1, n // 5))，A 为 1..10**7 之间的随机整数
    import random

    # 预处理部分：保持与原程序一致
    MAXA = 10 ** 7
    squares = set([i * i for i in range(1, 4000)])

    p = [i for i in range(MAXA + 1)]
    for i in range(1, MAXA + 1):
        if p[i] == i:
            for sq in squares:
                v = i * sq
                if v > MAXA:
                    break
                p[v] = i

    # 生成测试数据
    t = 1
    tests = []
    for _ in range(t):
        N = n
        K = min(20, max(1, N // 5))
        A = [random.randint(1, MAXA) for _ in range(N)]
        tests.append((N, K, A))

    # 正式逻辑：从 tests 中读取数据，模拟原来的多组输入
    outputs = []
    for (N, K, A) in tests:
        A = [p[A[i]] for i in range(N)]
        dp = [N] * (K + 1)
        dp[0] = 0
        used = [set() for _ in range(K + 1)]

        for i in range(N):
            x = A[i]
            for j in range(K, -1, -1):
                if dp[j] == N:
                    continue
                if x in used[j]:
                    if j < K and dp[j + 1] > dp[j]:
                        dp[j + 1] = dp[j]
                        used[j + 1] = set(used[j])
                    dp[j] += 1
                    used[j] = {x}
                else:
                    used[j].add(x)

        outputs.append(min(dp) + 1)

    # 返回结果列表，或者打印
    for ans in outputs:
        print(ans)


if __name__ == "__main__":
    # 示例：以 n = 100 运行
    main(100)