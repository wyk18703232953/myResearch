def A(n):
    return (4 ** n - 1) // 3


def main(n):
    L = 31

    # 生成规模为 n 的测试数据：
    # 这里假设测试数据为 n 组 (n_i, k_i)，其中：
    #   n_i 从 1 到 n
    #   k_i 取在 [1, A(min(n_i, L))] 范围内的一个中间值，保证有意义
    T = n
    test_cases = []
    for i in range(1, n + 1):
        ni = i
        ni_capped = min(ni, L)
        max_k = A(ni_capped)
        if max_k <= 0:
            ki = 1
        else:
            ki = max_k // 2
        test_cases.append((ni, ki))

    # 按原逻辑处理生成的测试数据
    for n_val, k in test_cases:
        n_cur = n_val

        if n_cur > L:
            print("YES", n_cur - 1)
            continue

        if k > A(n_cur):
            print("NO")
            continue

        E = 1
        M = 0
        R = 0
        while n_cur >= 0:
            M += E

            I = 2 * E - 1
            E = 2 * E + 1

            n_cur -= 1
            R += I * A(n_cur)

            if M <= k <= M + R:
                break

        if n_cur >= 0:
            print("YES", n_cur)
        else:
            print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5) 运行规模为 5 的测试
    main(5)