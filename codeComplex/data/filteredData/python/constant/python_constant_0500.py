def main(n):
    # 生成测试数据：
    # 这里生成 T = n 组测试，每组 (n_i, m_i, k_i)
    # 简单策略：
    #   n_i = i
    #   m_i = i // 2 + 1
    #   k_i = i + (i % 3)  （保证有大有小、有奇有偶）
    T = n

    for testCase in range(1, T + 1):
        ni = testCase
        mi = testCase // 2 + 1
        ki = testCase + (testCase % 3)

        # 原逻辑：
        n_val, m_val, k_val = ni, mi, ki
        min_k = max(n_val, m_val)
        if min_k > k_val:
            print(-1)
            continue
        if (n_val - m_val) % 2 == 0:
            if k_val % 2 == n_val % 2:
                print(k_val)
                continue
            print(k_val - 2)
            continue
        print(k_val - 1)


if __name__ == '__main__':
    # 示例：调用 main(5) 生成 5 组测试并输出
    main(5)