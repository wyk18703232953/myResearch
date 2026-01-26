def main(n):
    # 生成测试数据：构造 q 组 (n_i, k_i)
    # 这里简单生成 q = n 组数据，第 i 组为 (i+1, 2^(i+1)-1) 以及一些覆盖大规模的情况
    tests = []
    for i in range(1, n + 1):
        ni = i
        # 选一个适中的 k，保证覆盖各种情况
        if ni <= 20:
            ki = (1 << ni) - 1  # 2^ni - 1

        else:
            ki = (1 << 20) - 1  # 固定一个较大值，避免数值过大
        tests.append((ni, ki))
    # 再追加一些 n > 31 的测试
    tests.append((32, 100))
    tests.append((40, 10**9))

    q = len(tests)

    for case in range(q):
        n_case, k = tests[case]
        n_local = n_case  # 保留原始 n

        if n_local > 31:
            # print("YES", n_local - 1)
            pass
            continue

        a = [0]
        for i in range(1, n_local + 1):
            a.append(a[i - 1] * 4 + 1)

        if a[n_local] < k:
            # print("NO")
            pass
            continue

        if n_local == 2 and k == 3:
            # print("NO")
            pass
            continue

        p = 0
        q_val = 2
        n_work = n_local
        while p + q_val - 1 <= k and n_work > 0:
            p += q_val - 1
            q_val *= 2
            n_work -= 1
        # print("YES", n_work)
        pass
if __name__ == "__main__":
    # 示例运行：可以修改这里的 n 规模
    main(10)