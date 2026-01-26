def main(n):
    # n 作为规模参数，确定性地构造 a,b,c,d,e,f
    # 映射方案：六个线性函数和取模，所有依赖都只由 n 决定
    a = n
    b = n + 1
    c = n + 2
    d = n + 3
    e = (2 * n + 3) % (n + 5) + 1
    f = (3 * n + 1) % (n + 7) + 1

    n_val, n2 = 1, a * b + c * d + e * f
    while n_val ** 2 < n2:
        n_val += 1
    if n_val ** 2 > n2:
        print(-1)
        return
    l = sorted([[max(a, b), min(a, b), 'A'],
                [max(c, d), min(c, d), 'B'],
                [max(e, f), min(e, f), 'C']])
    if l[2][0] != n_val:
        print(-1)
        return
    v = str(n_val) + '\n' + (l[2][2] * n_val + '\n') * l[2][1]
    if l[0][0] == n_val and l[1][0] == n_val:
        for i in range(2):
            v += (l[i][2] * n_val + '\n') * l[i][1]
    else:
        s = n_val - l[2][1]
        if s not in l[0] or s not in l[1]:
            print(-1)
            return
        x = l[0][1] if l[0][0] == s else l[0][0]
        y = l[1][1] if l[1][0] == s else l[1][0]
        v += (l[0][2] * x + l[1][2] * y + '\n') * s
    print(v)


if __name__ == "__main__":
    # 示例：使用 n=10 作为规模
    main(10)