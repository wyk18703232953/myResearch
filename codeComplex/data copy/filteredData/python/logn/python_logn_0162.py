def main(n):
    # 生成测试数据：
    # 原程序中有两个输入 n, k，这里规模参数为 n，
    # 我们自行设定 k 的生成规则，例如 k = n（至少保证 k >= 1）
    k = max(1, n)

    # 原程序对 n, k 做了减一处理
    n_adj = n - 1
    k_adj = k - 1

    l = 0
    r = k_adj
    g = k_adj * (k_adj + 1) // 2
    ans = -1

    while l <= r:
        m = (l + r) // 2
        if g - m * (m + 1) // 2 >= n_adj:
            ans = k_adj - m
            l = m + 1

        else:
            r = m - 1

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)