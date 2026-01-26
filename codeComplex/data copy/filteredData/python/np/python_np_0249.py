def main(n):
    # 映射 n 为原程序中的 a,b,c,d,e,f
    # 为了可规模化且确定：让每个参数是 n 的简单函数
    a = n
    b = n + 1
    c = n + 2
    d = n + 3
    e = n + 4
    f = n + 5

    # 以下为原程序逻辑，去掉 input() 后直接使用上面的 a,b,c,d,e,f
    n_var, n2 = 1, a * b + c * d + e * f
    while n_var ** 2 < n2:
        n_var += 1
    if n_var ** 2 > n2:
        print(-1)
        return
    l = sorted([[max(a, b), min(a, b), 'A'],
                [max(c, d), min(d, c), 'B'],
                [max(e, f), min(e, f), 'C']])
    if l[2][0] != n_var:
        print(-1)
        return
    v = str(n_var) + '\n' + (l[2][2] * n_var + '\n') * l[2][1]
    if l[0][0] == n_var and l[1][0] == n_var:
        for i in range(2):
            v += (l[i][2] * n_var + '\n') * l[i][1]
    else:
        s = n_var - l[2][1]
        if s not in l[0] or s not in l[1]:
            print(-1)
            return
        if s != l[0][0]:
            l[0][0], l[0][1] = l[0][1], l[0][0]
        if s != l[1][0]:
            l[1][0], l[1][1] = l[1][1], l[1][0]
        v += (l[0][2] * l[0][1] + l[1][2] * l[1][1] + '\n') * s
    print(v)


if __name__ == "__main__":
    # 示例：用规模参数 n=10 调用
    main(10)