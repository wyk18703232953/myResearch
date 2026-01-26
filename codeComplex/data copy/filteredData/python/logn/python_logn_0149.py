def main(n):
    # 将 n 同时映射为原始输入规模的两个参数
    # 原代码读入: n, k，然后变为 n-1, k-1
    # 这里令原始输入为: N = n + 1, K = n + 1
    # 则变换后: n2 = n, k2 = n
    n2 = n
    k2 = n

    n2, k2 = n2 - 1, k2 - 1
    l = 0
    r = k2
    g = k2 * (k2 + 1) // 2
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if (g - m * (m + 1) // 2) >= n2:
            ans = k2 - m
            l = m + 1

        else:
            r = m - 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)