def main(n):
    # 预处理 pw
    pw = [1, 4]
    for i in range(2, 32):
        pw.append(pw[i - 1] * 4)

    # 根据规模 n 生成测试数据：
    # 构造 t 组 (n_i, k_i)，其中 n_i 与参数 n 相关，k_i 为某种分布
    tests = []
    t = n  # 测试组数与规模相同
    for i in range(1, t + 1):
        # 示例生成方式：
        # n_i 在 [1, n] 内波动，k_i 在 [1, 4^10] 内取一个相对合理的范围
        n_i = i
        k_i = i * 3
        tests.append((n_i, k_i))

    # 处理逻辑
    results = []
    for (n_val, k_val) in tests:
        n, k = n_val, k_val
        last = 1
        path = 1
        ans = n
        i = 0
        while True:
            if ((pw[i + 1] - 1) // 3 > k):
                ans -= i
                last = k - (pw[i] - 1) // 3
                break
            i = i + 1
            path *= 2
            # 防止极端情况死循环
            if i + 1 >= len(pw):
                ans -= i
                last = k - (pw[i] - 1) // 3
                break

        sp = path * 2 - 1
        if (ans < 0) or ((ans == 0) and (last > 0)):
            results.append("No")
            continue
        sq = path * path - sp
        if (ans == 1) and (last > sq) and (last < sp):
            results.append("No")
            continue
        elif (ans == 1) and (last >= sp):
            ans = ans - 1
        results.append(f"Yes {ans}")

    # 输出结果
    for line in results:
        # print(line)
        pass
if __name__ == "__main__":
    # 示例调用：规模 n = 5
    main(5)