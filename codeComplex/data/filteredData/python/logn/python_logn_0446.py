def sol(n, k):
    p = 1
    q = 1
    acc = 0
    while n > 0 and k >= p:
        k -= p
        n -= 1
        if n >= 40:
            return n
        acc += q * (4 ** n - 1) // 3
        if k <= acc:
            return n
        p = 2 * p + 1
        q = 2 * q + 3
    return -1


def main(t):
    """
    t: 测试组数规模，用来生成 t 组 (n, k) 测试数据并运行 sol。
    测试数据生成策略：
      - n 在 [1, 50] 范围内
      - k 在 [1, 10**6] 范围内
    """
    import random

    random.seed(0)
    for _ in range(t):
        n = random.randint(1, 50)
        k = random.randint(1, 10**6)
        ans = sol(n, k)
        if ans == -1:
            print("NO")
        else:
            print("YES", ans)


if __name__ == "__main__":
    # 示例：规模 t = 5
    main(5)