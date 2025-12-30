def main(n):
    # 预计算 f 序列
    N = 55
    f = [0]
    for i in range(1, N):
        f.append(f[-1] * 4 + 1)
        if f[-1] > 1e18:
            break

    # 生成测试数据：构造若干 (n, m) 对
    # 这里固定生成 10 组数据，可根据需要自行调整
    import random
    random.seed(0)

    test_cases = []
    for _ in range(10):
        if n <= 0:
            cur_n = 1
        else:
            cur_n = random.randint(1, max(1, n))
        # 大致给 m 一个范围：依据原逻辑中 start/end 的数量级粗略设定
        # 对于较大的 n 给更大的 m 范围
        if cur_n > 31:
            # 对大 n，随便给一个大一点的 m
            cur_m = random.randint(1, 10**12)
        else:
            # 对于 n<=31，给一个相对小一点的 m 范围
            cur_m = random.randint(1, 10**6)
        test_cases.append((cur_n, cur_m))

    # 运行原逻辑
    outputs = []
    for (n_val, m_val) in test_cases:
        if n_val > 31:
            outputs.append("YES {}".format(n_val - 1))
        else:
            # n <= 31
            start = 0
            found = False
            res = -1
            for i in range(1, n_val + 1):
                start += 2**i - 1
                end = start
                for k in range(1, i + 1):
                    # 注意 f 的长度可能小于 n_val，需要防御
                    idx = n_val - k
                    if idx < 0 or idx >= len(f):
                        end = float('inf')
                        break
                    end += f[idx] * (2**(k + 1) - 3)
                if m_val >= start and m_val <= end:
                    found = True
                    res = i
                    break
            if found:
                outputs.append("YES {}".format(n_val - res))
            else:
                outputs.append("NO")

    # 输出结果
    # 为了可重复使用，main(n) 既打印也返回结果列表
    for line in outputs:
        print(line)
    return outputs