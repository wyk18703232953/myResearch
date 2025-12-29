def main(n):
    # 根据规模 n 生成测试数据 (l, r)
    # 这里简单生成：l 为 0，r 为 (1 << n) - 1，且 n 不超过 62
    n = min(n, 62)
    l = 0
    r = (1 << n) - 1

    a = "{0:062b}".format(l)
    b = "{0:062b}".format(r)

    length = len(a)
    i = 0

    if l == r:
        print(0)
    else:
        while i < length and a[i] == b[i]:
            i += 1
        print(2 ** (62 - i) - 1)


if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(10)