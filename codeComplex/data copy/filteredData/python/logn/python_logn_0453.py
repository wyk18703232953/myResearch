def main(n):
    # 生成测试数据：构造 n 组 (n_i, k_i)
    # 这里简单生成：n_i = i+2（从 2 开始递增），k_i = 2*i+3
    # 你可以根据需要自行调整生成规则
    test_cases = []
    for i in range(n):
        ni = i + 2           # 保证 n >= 2
        ki = 2 * i + 3       # 一些随规模变化的 k
        test_cases.append((ni, ki))

    # 原逻辑处理每个测试用例
    for n_val, k_val in test_cases:
        n_i, k_i = n_val, k_val
        if (n_i == 2 and k_i == 3) or (n_i <= 30 and k_i > (4 ** n_i - 1) // 3):
            # print('NO')
            pass

        else:
            cn = n_i - 1
            ck = k_i - 1
            l = 1
            while cn * ck != 0 and ck >= 4 * l - 1:
                ck -= 4 * l - 1
                cn -= 1
                l *= 2
            # print('YES', cn)
            pass
if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改
    main(5)