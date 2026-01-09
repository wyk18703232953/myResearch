def main(n):
    # 映射：n 为数组长度
    m = n

    # 确定性构造数组 a 和 b
    # a: [0, 1, 2, ..., n-1]
    a = list(range(n))
    # b: 每个元素为 (i * 2) % n，保证确定性且有交集
    b = [(i * 2) % n for i in range(m)]

    r = []
    for i in a:
        if i in b:
            r.append(i)
    # print(' '.join(map(str, r)))
    pass
if __name__ == "__main__":
    main(10)