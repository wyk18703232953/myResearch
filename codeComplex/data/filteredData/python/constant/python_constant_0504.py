def main(n):
    import random

    # 生成测试数据：构造 n 组 (n_i, m_i, k_i)
    # 这里将每个值的绝对值控制在 0~n 范围内
    test_cases = []
    for _ in range(n):
        ni = random.randint(-n, n)
        mi = random.randint(-n, n)
        # 保证 k 足够大以覆盖部分情况，同时有一定概率 < |n| 或 |m|
        ki = random.randint(0, 2 * n)
        test_cases.append((ni, mi, ki))

    # 处理逻辑（原来的 for _ in range(int(input()))）
    for ni, mi, ki in test_cases:
        a = abs(ni)
        b = abs(mi)
        k = ki
        if max(a, b) > k:
            print("-1")
        else:
            bad1 = ((a + k) % 2 == 1)
            bad2 = ((b + k) % 2 == 1)
            print(k - bad1 - bad2)


if __name__ == "__main__":
    # 示例：规模参数 n，可根据需要调整
    main(10)