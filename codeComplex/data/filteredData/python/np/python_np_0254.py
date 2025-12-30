def main(n):
    # 根据规模 n 生成一组 (a, b, c, d, e, f)
    # 让总面积为 n^2，且能成功铺满
    #
    # 构造方案：
    # 顶部用 A 覆盖一整行：A: n x 1
    # 中间用 B、C 各覆盖若干行，总高度为 n-1
    # 取 B: n x (n//2), C: n x (n-1-n//2)
    a, b = n, 1
    c, d = n, n // 2
    e, f = n, n - 1 - n // 2

    # 原程序逻辑开始
    n1 = a * b + c * d + e * f
    n_side = 1
    while n_side ** 2 < n1:
        n_side += 1
    if n_side ** 2 > n1:
        print(-1)
        return

    l = sorted([[max(a, b), min(a, b), 'A'],
                [max(c, d), min(c, d), 'B'],
                [max(e, f), min(e, f), 'C']])
    if l[2][0] != n_side:
        print(-1)
        return

    v = str(n_side) + '\n' + (l[2][2] * n_side + '\n') * l[2][1]
    if l[0][0] == n_side and l[1][0] == n_side:
        for i in range(2):
            v += (l[i][2] * n_side + '\n') * l[i][1]
    else:
        s = n_side - l[2][1]
        if s not in l[0] or s not in l[1]:
            print(-1)
            return
        x = l[0][1] if s == l[0][0] else l[0][0]
        y = l[1][1] if s == l[1][0] else l[1][0]
        v += (l[0][2] * x + l[1][2] * y + '\n') * s
    print(v)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)