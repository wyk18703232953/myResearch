def main(n):
    # 依据规模 n 生成测试数据，这里构造 t 组 (n_i, k_i)
    # 示例策略：n_i 从 1 到 n，k_i 取若干典型值
    test_cases = []
    for ni in range(1, n + 1):
        # 构造三个不同的 k 进行测试：
        ks = [0, 1, 2 ** (ni // 2) if ni > 0 else 0]
        for k in ks:
            test_cases.append((ni, k))

    # 处理测试数据
    for n_val, k in test_cases:
        if n_val > 31:
            # print('YES ' + str(n_val - 1))
            pass

        else:
            rez = -1
            for i in range(1, n_val + 1):
                x = (4 ** i - 2 ** (i + 1) + 1) * ((4 ** (n_val - i) - 1) // 3) + (4 ** i - 1) // 3
                y = (4 ** i - 1) // 3 - (4 ** (i - 1) - 1) // 3
                if y <= k <= x:
                    rez = n_val - i
                    break
            # print('YES ' + str(rez) if rez != -1 else 'NO')
            pass
if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改规模
    main(5)