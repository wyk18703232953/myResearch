def main(n: int):
    # 预计算每段长度的累计位数边界
    # li1[i] 表示从 1 位数到 i 位数所有数字的总位数
    a, b, c, d, e, f, g, h, i, j, k, l = [
        9 * 1,
        90 * 2,
        900 * 3,
        9000 * 4,
        90000 * 5,
        900000 * 6,
        9000000 * 7,
        90000000 * 8,
        900000000 * 9,
        9000000000 * 10,
        90000000000 * 11,
        900000000000 * 12,
    ]
    a = a
    b = a + b
    c = b + c
    d = c + d
    e = d + e
    f = e + f
    g = f + g
    h = g + h
    i = h + i
    j = i + j
    k = j + k
    l = k + l
    li1 = [0, a, b, c, d, e, f, g, h, i, j, k, l]

    nn = 0
    for ii in range(1, 12):
        if li1[ii - 1] < n and li1[ii + 1] > n:
            nn = ii
            break

    # n 落在 nn 位数区间内
    n = n - li1[nn - 1]        # 去掉前面所有位数段
    r1 = 10 ** (nn - 1)        # nn 位数的起始数字
    n1 = n // nn               # 从起始数字算起跨过的完整数字数量
    r1 += n1 - 1               # 当前完整数字的值
    n2 = n - (n1 * nn)         # 在当前（或下一个）数字内的第几位

    if n2 == 0:
        # print(str(r1)[-1])
        pass

    else:
        # print(str(r1 + 1)[n2 - 1])
        pass
if __name__ == "__main__":
    # 示例：根据规模 n 自动生成测试调用
    # 可以根据需要修改下面的测试用例
    test_n = 1000
    main(test_n)