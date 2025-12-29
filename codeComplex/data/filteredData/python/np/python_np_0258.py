def chnge(last, cap, ini=(0, 0), fin=None):
    for i in range(ini[1], last[1]):
        fin[i][ini[0]:last[0]] = [cap] * (last[0] - ini[0])


def main(n):
    """
    规模 n：用于生成测试数据 (x1,y1,x2,y2,x3,y3)，
    使得三个矩形可以刚好拼成一个 m×m 的正方形。
    """
    # 简单的测试数据生成策略：
    # 1. 将 n 分成三部分 a,b,c，令 a+b+c = n
    # 2. 正方形边长 m = n
    # 3. 三个矩形：a×n, b×n, c×n
    #    总面积 = (a+b+c)*n = n*n = m*m
    #
    # 为避免 degenerate 情况，要求 n >= 3
    if n < 3:
        # 退化到固定可行用例：3×3 的三块 1×3、1×3、1×3
        x1, y1 = 1, 3
        x2, y2 = 1, 3
        x3, y3 = 1, 3
    else:
        # 简单拆分：1 + 1 + (n-2)
        a = 1
        b = 1
        c = n - 2
        m = n
        # 三个矩形尺寸：(a×m), (b×m), (c×m)
        x1, y1 = a, m
        x2, y2 = b, m
        x3, y3 = c, m

    # 以下为原逻辑（用生成的 x1..y3 代替 input）

    global fin  # 供 chnge 使用
    a = (max(x1, y1), [x1, y1], "A")
    b = (max(x2, y2), [x2, y2], "B")
    c = (max(x3, y3), [x3, y3], "C")
    m = max(a[0], b[0], c[0])
    fin = [["*" for _ in range(m)] for _ in range(m)]

    if (x1 * y1 + x2 * y2 + x3 * y3) != m ** 2:
        print(-1)
        return

    l = sorted([a, b, c], reverse=True)
    l[0][1].sort(reverse=True)
    chnge(l[0][1], l[0][2], fin=fin)

    ini = [0, l[0][1][1]]
    last = l[1][1]
    if m in [ini[0] + last[0], ini[1] + last[1]] and \
       (ini[0] + last[0] + ini[1] + last[1]) <= 2 * m:
        last = [ini[0] + last[0], ini[1] + last[1]]
    else:
        last = [ini[0] + last[1], ini[1] + last[0]]

    chnge(last, l[1][2], ini, fin=fin)
    chr_fill = l[2][2]

    print(m)
    for row in fin:
        print("".join(row).replace("*", chr_fill))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)