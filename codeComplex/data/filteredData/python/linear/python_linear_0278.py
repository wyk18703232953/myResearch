def main(n):
    # 将 n 映射为原程序中的 n, m, a, b
    # 保证可规模化：m, a, b 随 n 线性增长，并且为正整数
    N = n
    M = max(1, n + 1)      # 保证 m > 0，且随 n 增长
    A = n + 2
    B = n + 3

    n_val, m_val, a_val, b_val = N, M, A, B

    if n_val % m_val == 0:
        print(0)
    else:
        k = n_val % m_val
        print(min(k * b_val, (m_val - k) * a_val))


if __name__ == "__main__":
    main(10)