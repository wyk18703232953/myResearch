def A(n):
    return (4 ** n - 1) // 3


L = 31


def main(n):
    # 生成规模为 n 的测试数据：
    # 构造 T 组 (n_i, k_i)，这里让 n_i 在 [1, min(n, 40)] 内，
    # k_i 在 [1, A(n_i)] 或略大于 A(n_i)，以覆盖 YES/NO 分支。
    T = n
    test_cases = []
    for i in range(1, T + 1):
        ni = (i % 40) + 1  # 保证 n_i 不太大，覆盖 n > L 和 n <= L 情况
        if i % 3 == 0:
            # 让 k 大于 A(ni)，使其走 NO 分支
            ki = A(ni) + i

        else:
            # 让 k 落在 [1, A(ni)]，多数情况在合法区间内
            ki = max(1, (A(ni) * (i % 10 + 1)) // 10)
        test_cases.append((ni, ki))

    # 原逻辑主体
    results = []
    for n_i, k in test_cases:
        n_local = n_i

        if n_local > L:
            results.append(f"YES {n_local - 1}")
            continue

        if k > A(n_local):
            results.append("NO")
            continue

        E = 1
        M = 0
        R = 0
        while n_local >= 0:
            M += E

            I = 2 * E - 1
            E = 2 * E + 1

            n_local -= 1
            R += I * A(n_local)

            if M <= k <= M + R:
                break

        if n_local >= 0:
            results.append(f"YES {n_local}")

        else:
            results.append("NO")

    # 输出结果
    for line in results:
        # print(line)
        pass
if __name__ == "__main__":
    # 示例：调用 main(5) 运行规模为 5 的测试
    main(5)