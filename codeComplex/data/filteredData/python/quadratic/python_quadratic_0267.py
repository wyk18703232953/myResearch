def main(n):
    # n 表示两个数组的长度，规模一致为 n
    m = n
    # 确定性生成 a 和 b
    a = [i for i in range(n)]
    b = [(2 * i + 1) % (n + 3) for i in range(m)]
    lst = []
    for i in range(len(a)):
        if a[i] in b:
            lst.append(a[i])
    if len(lst) == 0:
        pass
    else:
        print(*lst)


if __name__ == "__main__":
    main(10)