def main(n):
    # 生成测试数据：根据题意原代码中还需一个 m，从 1 到 2^n 取一个合理值
    # 这里简单选取 m = 2^n // 2 + 1（若无特别要求可自行调整）
    m = (1 << n) // 2 + 1
    m += 1  # 与原程序一致，先读入 m 然后 m += 1

    # calc 使用到的外部变量：s, f
    def calc(l, r, eq, eq_i):
        if l > r:
            return 1
        key = (l, eq, eq_i)
        if key in f:
            return f[key]

        t = 0
        for x in (['0', '1'] if s[l] == '?' else [s[l]]):
            if l == r:
                a = [x]
            else:
                a = ['0', '1'] if s[r] == '?' else [s[r]]
            for y in a:
                if not ((eq and x > y) or (eq_i and x == y == '1')):
                    t += calc(l + 1, r - 1, eq and x == y, eq_i and x != y)
        f[key] = t
        return t

    s = ['?'] * n
    for i in range(n):
        s[i] = '0'
        f = {}
        p = calc(0, n - 1, True, True)
        if m > p:
            m -= p
            s[i] = '1'

    if s[0] == '0':
        print(''.join(s))
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)