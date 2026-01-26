def main(n):
    # 将 n 映射为输入规模
    # 保证 m 与 n 同规模，元素范围略大于 n 以产生部分交集
    if n <= 0:
        return

    m = n

    # 构造确定性的列表 a 与 b
    # a: [0, 1, 2, ..., n-1]
    a = list(range(n))
    # b: [(i * 2) % (n + 3) for i in range(m)]
    b = [(i * 2) % (n + 3) for i in range(m)]

    r = []
    for i in a:
        if i in b:
            r.append(i)

    if r:
        # print(' '.join(map(str, r)))
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(10)