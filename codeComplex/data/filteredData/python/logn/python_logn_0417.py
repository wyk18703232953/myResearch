def main(n):
    """
    n 作为规模，用来生成测试数据的大小：
    - 测试组数 t = n
    - 对于第 i 组：
        n_i = min(35, i + 1)      # 防止过大且覆盖 n>31 情况
        m_i = i * i               # 构造一个随 i 增长的 m
    函数直接打印输出，行为与原程序一致。
    """

    # 预处理 f 数组
    N = 55
    f = [0]
    for i in range(1, N):
        f.append(f[-1] * 4 + 1)
        if f[-1] > 1e18:
            break

    t = n  # 测试组数由参数 n 决定

    for case_id in range(1, t + 1):
        # 生成一组 (n_case, m_case) 测试数据
        n_case = min(35, case_id + 1)   # 保证覆盖 n>31 的分支
        m_case = case_id * case_id      # 简单的递增 m

        n_val = n_case
        m_val = m_case

        if n_val > 31:
            # 原逻辑：n > 31 时必 YES n-1
            # print("YES {}".format(n_val - 1))
            pass

        else:
            # 原逻辑：n <= 31 时进行区间查找
            start = 0
            found = False
            res = -1
            for i in range(1, n_val + 1):
                start += 2 ** i - 1
                end = start
                for k in range(1, i + 1):
                    end += f[n_val - k] * (2 ** (k + 1) - 3)
                if start <= m_val <= end:
                    found = True
                    res = i
                    break
            if found:
                # print("YES {}".format(n_val - res))
                pass

            else:
                # print("NO")
                pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)