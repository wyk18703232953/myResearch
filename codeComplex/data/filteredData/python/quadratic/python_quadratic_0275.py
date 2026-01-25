def main(n):
    # n 表示每个列表的长度
    a = n
    b = n

    # 确定性生成 c 和 d
    # c: 0, 1, 2, ..., n-1
    c = [i for i in range(a)]
    # d: 0, 2, 4, ..., 2(n-1)
    d = [2 * i for i in range(b)]

    e = []
    for i in c:
        if i in d:
            e.append(i)
    for j in e:
        print(j, end=" ")
    print()


if __name__ == "__main__":
    main(10)