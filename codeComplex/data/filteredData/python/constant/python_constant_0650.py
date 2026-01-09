def main(n: int):
    # 预处理 f
    f = [0 for _ in range(40)]
    for i in range(1, 32):
        f[i] = 1 + 4 * f[i - 1]

    # 生成测试数据：构造若干 (n_i, k) 测试
    # 这里简单使用与规模 n 相关的一些样例
    tests = []

    # 1) 使用参数 n 本身
    if n <= 0:
        return
    base_n = n
    if base_n >= 40:
        base_n = 39

    # 合理的 k 范围：1 到 f[min(base_n, 31)] + 若干
    max_idx = min(base_n, 31)
    max_f = f[max_idx] if max_idx >= 0 else 0

    # 添加若干测试样例
    # 样例1：k = 1
    tests.append((base_n, 1))
    # 样例2：k = max_f // 2 (如果 > 0)
    if max_f > 1:
        tests.append((base_n, max_f // 2))
    # 样例3：k = max_f
    if max_f > 0:
        tests.append((base_n, max_f))
    # 样例4：k = max_f + 1，测试 NO 情况
    tests.append((base_n, max_f + 1))
    # 再添加一些固定小规模用例
    tests.append((5, 3))
    tests.append((10, 100))
    tests.append((31, f[31]))
    tests.append((32, 1))
    tests.append((35, 10**18))  # 大 k 测试

    # 去重
    tests = list(dict.fromkeys(tests))

    # 按原逻辑处理所有测试
    for n_i, k in tests:
        if n_i >= 32:
            # 原逻辑：直接 YES n-1
            # print("YES %d" % (n_i - 1))
            pass
            continue

        if n_i < 0:
            # print("NO")
            pass
            continue

        if f[n_i] < k:
            # print("NO")
            pass
            continue

        k -= 1
        extra = 1
        way = 3
        size = n_i - 1
        total = f[size] if size >= 0 else 0
        ans = True

        while k > total and size > 0:
            if k < way:
                ans = False
                break
            k -= way
            size -= 1
            extra = way * 2 - 1
            way = way * 2 + 1
            total += extra * f[size]

        if ans:
            # print("YES %d" % size)
            pass

        else:
            # print("NO")
            pass


# 示例运行
if __name__ == "__main__":
    # 可修改 20 为任意规模 n
    main(20)