def main(n):
    # 将 n 解释为问题规模，构造确定性输入 (N, M, A, B)
    # 这里令:
    # N = n
    # M = 2*n + 1
    # A = n % 7 + 1
    # B = n % 5 + 1
    N = n
    M = 2 * n + 1
    A = n % 7 + 1
    B = n % 5 + 1

    # 原有核心逻辑
    n_val, m_val, a_val, b_val = N, M, A, B
    if n_val > m_val:
        if n_val % m_val == 0:
            print(0)
        else:
            t1 = n_val % m_val
            print(min(t1 * b_val, (m_val - t1) * a_val))
    elif n_val == m_val:
        print(0)
    else:
        print(min(n_val * b_val, (m_val - n_val) * a_val))


if __name__ == "__main__":
    # 示例：以 10 作为规模参数运行
    main(10)