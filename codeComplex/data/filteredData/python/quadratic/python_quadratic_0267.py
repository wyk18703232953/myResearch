def main(n):
    # 映射：n 为数组长度，m 固定为 n
    m = n

    # 确定性生成数据：
    # a: [0, 1, 2, ..., n-1]
    # b: [i % (n // 2 + 1) for i in range(n)]
    a = list(range(n))
    b = [(i * 2 + 3) % (n // 2 + 1 if n // 2 + 1 > 0 else 1) for i in range(m)]

    lst = []
    for i in range(len(a)):
        if a[i] in b:
            lst.append(a[i])
    if len(lst) == 0:
        pass

    else:
        # print(*lst)
        pass
if __name__ == "__main__":
    main(10)