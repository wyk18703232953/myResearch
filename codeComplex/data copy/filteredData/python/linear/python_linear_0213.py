def main(n):
    # 由 n 确定性生成输入规模和数据
    # 映射规则：
    #   原程序第一行: n, A, C
    #   原程序后续 n 行: z, x, y
    #
    # 这里将:
    #   n_lines = max(1, n)
    #   A = n + 1
    #   C = 2 * n + 3
    #   对于第 i 行 (0 <= i < n_lines):
    #       z = i
    #       x = (i * 2 + 1)
    #       y = (i * i + 3)
    #
    # 以上构造完全由 n 决定，满足确定性和可重复。

    n_lines = max(1, n)
    A = n + 1
    C = 2 * n + 3

    def Ro(x, y):
        return A * x - y + C

    huh = []
    for i in range(n_lines):
        z = i
        x = i * 2 + 1
        y = i * i + 3
        huh.append((Ro(x + z, z * A + y), x))

    huh = sorted(huh)
    anss = 0
    c1 = 0
    c2 = 0
    prev = (-9999999999999, -999999999999999)
    g = []

    huh.append((-9999999999999, -999999999999999))

    for huhh in huh:
        if huhh[0] != prev[0]:
            g.append(c1)
            for j in g:
                anss += (c2 - j) * j
            g = []
            c1 = 1
            c2 = 1
            prev = (huhh[0], huhh[1])
            continue
        c2 += 1
        if huhh[1] != prev[1]:
            g.append(c1)
            c1 = 0
            prev = (huhh[0], huhh[1])
        c1 += 1

    # print(anss)
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 以进行规模实验
    main(10)