def main(n):
    # 解释输入结构映射：
    # 原程序输入为：n, m, k 和一个长度为 m 的数组 p
    # 这里新的 main(n) 中参数 n 作为 m 的规模含义
    # 我们将：
    #   m = n
    #   k = max(1, n // 3) 保证随规模变化，且不为 0
    #   n_input = n 作为第一个整数（与规模同名但仅作为原程序的第一个输入）
    #
    # p 需要是一个严格递增且正整数的数组，以保证原逻辑合理：
    #   p[i] = (i + 1) * 2
    # 这样生成的数据是完全确定性的，且单调递增
    n_input = n
    m = n
    k = max(1, n // 3)

    p = [(i + 1) * 2 for i in range(m)]

    i = 0
    c = 0
    d = 0
    while i < m:
        c = c + 1
        d2 = d
        x = k * ((p[i] - d2 - 1) // k) + k
        while i < m and p[i] - d2 <= x:
            i = i + 1
            d = d + 1
            if i == m:
                break
    # print(c)
    pass
if __name__ == "__main__":
    main(10)