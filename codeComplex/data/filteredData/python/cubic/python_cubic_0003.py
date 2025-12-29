def raschot(d, e, g, h, a0, b):
    if d > e:
        return 1
    key = (d, g, h)
    if key in b:
        return b[key]
    f = 0
    for x in (['0', '1'] if a0[d] == '?' else [a0[d]]):
        if d == e:
            a = [x]
        else:
            a = ['0', '1'] if a0[e] == '?' else [a0[e]]
        for y in a:
            if not ((g and x > y) or (h and x == y == '1')):
                f += raschot(d + 1, e - 1, g and x == y, h and x != y, a0, b)
    b[key] = f
    return f


def main(n):
    # 生成测试数据：给定规模 n，构造一个 m 值
    # 这里简单设置为某个相对较大的数，以测试逻辑
    m = n * n + 5  # 可根据需要调整测试数据生成方式

    m += 1
    a0 = ['?'] * n
    for i in range(n):
        a0[i] = '0'
        b = {}
        c = raschot(0, n - 1, True, True, a0, b)
        if m > c:
            m -= c
            a0[i] = '1'
    if a0[0] == '0':
        print(''.join(a0))
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改测试规模
    main(5)