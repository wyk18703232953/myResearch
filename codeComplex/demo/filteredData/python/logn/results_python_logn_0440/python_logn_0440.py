def main(n):
    """
    将原始含 input() 的程序改写为：
    - 无 input()
    - main(n) 为入口，其中 n 作为规模参数
    - 自动生成测试数据 (test 组，(n_i, k_i) 每组)
    - 执行原始逻辑并打印结果

    这里的“规模 n”用于控制测试数据数量和每组数据的规模。
    生成规则示例（可根据需要修改）：
    - test = n
    - 第 i 组：n_i = max(1, i)  (从 1 到 n)
                k_i = 2 ** i    (随 i 指数增长)
    """

    # 生成测试数据：test 组，每组 (n_i, k_i)
    test = n
    test_cases = []
    for i in range(1, test + 1):
        n_i = max(1, i)      # 保证 n_i >= 1
        k_i = 2 ** i         # 使 k 随 i 变化
        test_cases.append((n_i, k_i))

    # 原程序逻辑封装为一个函数，便于调用和检查
    def solve_single_case(n_local, k_local):
        s = 0
        curr = 1
        ct = 0
        # 第一段 while：根据 k_local 快速判断
        while s < k_local:
            s = s + curr
            curr = 4 * curr
            ct = ct + 1

        if n_local >= 35:
            # 原逻辑：直接 YES n-1
            # print("YES", n_local - 1)
            pass
            return

        # 构造 val 数组
        val = [0]
        for i in range(1, n_local):
            val.append(1 + 4 * val[i - 1])

        s = 0
        t = 2
        rem = 0

        # 注意：这里的 n_local 在循环中会递减
        while n_local > 0:
            s = s + t - 1
            t *= 2
            rem = rem + (t - 3) * (val[n_local - 1])
            rem = int(rem)
            if rem + s >= k_local and s <= k_local:
                # print("YES", n_local - 1)
                pass
                n_local = -2   # 用作标记，表示已经找到
                break
            n_local = n_local - 1

        if n_local != -2:
            # print("NO")
            pass

    # 依次处理每一组测试数据
    for n_i, k_i in test_cases:
        solve_single_case(n_i, k_i)


if __name__ == "__main__":
    # 示例：调用 main(5)，会自动生成 5 组测试数据并输出结果
    main(5)