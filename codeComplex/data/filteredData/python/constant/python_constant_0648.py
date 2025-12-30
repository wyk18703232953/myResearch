def main(n):
    """
    将原始交互式程序改为参数化版本：
    - n: 测试组数量
    - 自动生成 n 组 (n_i, k_i) 测试数据并打印结果
    """

    # 预处理 pw 数组
    pw = [1, 4]
    for i in range(2, 32):
        pw.append(pw[i - 1] * 4)

    # 生成测试数据：这里采用简单的规则生成 (n_i, k_i)
    # 可根据需要自行调整生成策略
    test_cases = []
    for i in range(1, n + 1):
        # n_i 取一个适中范围，k_i 与几何级数相关
        ni = 10 + i              # 保证 n_i >= 10
        ki = i * 5               # 让 k 随 i 增长
        test_cases.append((ni, ki))

    # 按原逻辑处理每个用例
    for (n_val, k) in test_cases:
        last = 1
        path = 1
        ans = n_val
        i = 0
        while True:
            if (pw[i + 1] - 1) // 3 > k:
                ans -= i
                last = k - (pw[i] - 1) // 3
                break
            i = i + 1
            path *= 2

        sp = path * 2 - 1
        if (ans < 0) or ((ans == 0) and (last > 0)):
            print("No")
            continue

        sq = path * path - sp
        if (ans == 1) and (last > sq) and (last < sp):
            print("No")
            continue
        elif (ans == 1) and (last >= sp):
            ans = ans - 1

        print("Yes", ans)


if __name__ == "__main__":
    # 示例：运行 5 组测试
    main(5)