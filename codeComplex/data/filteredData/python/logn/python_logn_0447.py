def sol(n, k):
    p = 1
    acc = 0
    while n > 0 and k >= p:
        k -= p
        n -= 1
        if n >= 40:
            return n
        acc += (2 * p - 1) * (4 ** n - 1) // 3
        if k <= acc:
            return n
        p = 2 * p + 1
    return -1


def main(n):
    """
    n 为测试规模，这里根据 n 生成 n 组 (n_i, k_i) 测试数据并运行。
    测试数据生成策略可按需调整。
    """
    # 生成测试数据：第 i 组为 (n_i, k_i)
    tests = []
    for i in range(1, n + 1):
        # n_i 在 [1, 50] 内循环
        ni = 1 + (i % 50)
        # k_i 简单设为一个随 i 增长的数，保证范围合理
        ki = i * i
        tests.append((ni, ki))

    # 执行测试并输出
    for ni, ki in tests:
        ans = sol(ni, ki)
        if ans == -1:
            print("NO")
        else:
            print("YES", ans)


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)