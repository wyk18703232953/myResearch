def main(n):
    # 映射规则：
    # n -> n（规模参数）
    # 构造：
    #   m = n（元素个数）
    #   k = max(1, n // 3)
    #   n_val = n
    #   p 为长度为 m 的严格递增序列
    m = n
    if m <= 0:
        # print(0)
        pass
        return
    k = max(1, n // 3)
    n_val = n
    # 确定性构造递增序列 p
    # p[i] = i + 1 + (i // 2)，保证严格递增且可控
    p = [i + 1 + (i // 2) for i in range(m)]

    i = 0
    c = 0
    d = 0
    while i < m:
        c = c + 1
        d2 = d
        x = k * ((p[i] - d2 - 1) // k) + k
        while p[i] - d2 <= x:
            i = i + 1
            d = d + 1
            if i == m:
                break
    # print(c)
    pass
if __name__ == "__main__":
    main(10)