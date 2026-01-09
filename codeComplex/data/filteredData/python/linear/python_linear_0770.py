def main(n):
    # n 作为数组长度，也是 m；k 取一个与 n 相关的值，确保确定性
    m = n
    k = max(1, n // 3)

    # 构造一个严格递增的数组 l，模拟原来从输入读入的删除位置等场景
    # 确保所有值在 1..n+k 范围内，并递增
    l = [(i + 1) + (i // 2) for i in range(m)]

    out = 0
    d = 0

    while m > d:
        nex = l[d]
        page = (nex - d - 1) // k
        add = 1
        while d + add < m and (page * k) < l[d + add] - d <= (page + 1) * k:
            add += 1
        d += add
        out += 1

    # print(out)
    pass
if __name__ == "__main__":
    main(10)