def main(n):
    """
    n: 规模参数，用来生成测试数据的数量 T 和每组 (n_i, k_i)
    这里的 n 并不是原始代码中的 n_i，而是用于构造测试数据的“外部规模”。
    """

    # -------------------------
    # 生成测试数据：T 组 (n_i, k_i)
    # 规则（可根据需要调整）：
    #   T = n
    #   对于第 i 组：
    #       n_i 在 [1, max(1, n)] 内变化
    #       k_i 简单构造为 1 + (i * 7)（保证有大有小）
    # -------------------------
    T = n if n > 0 else 1
    queries = []
    for i in range(1, T + 1):
        ni = i  # 简单设为从 1 到 T
        ki = 1 + i * 7
        queries.append((ni, ki))

    # -------------------------
    # 核心逻辑从原程序移植
    # -------------------------
    def process_case(n_i, k_i):
        n = n_i
        k = k_i

        if n < 32 and (4 ** n) < 3 * k:
            return "NO"

        now = 1
        p = 2
        ans = n
        sq = 0
        buff = 0
        d = 4

        while k >= now:
            k -= now
            p *= 2
            now = p - 1
            ans -= 1

            sq = sq * 4 + d - 3
            d *= 2
            if n < 60:
                buff += sq * (4 ** ans - 1) // 3
            else:
                buff = 10 ** 19

            if ans == 0:
                break

        if buff < k:
            return "NO"
        else:
            return "YES " + str(max(ans, 0))

    # 执行所有测试用例并输出
    for n_i, k_i in queries:
        print(process_case(n_i, k_i))


if __name__ == "__main__":
    # 示例：调用 main(3) 近似对应原始示例中 3 组测试
    main(3)