def main(n):
    # 映射规则：
    # 原程序有两个输入 n, m
    # 这里将输入规模参数 n 拆成：
    #   N = n（原始的 n）
    #   M = (n % 5) + 1  保证 M 在 [1,5]，同时完全确定性
    N = n
    M = (n % 5) + 1

    a = []
    b = []
    check = True
    while N >= 0:
        if check is True:
            a.append(5)
            N -= 5
            b.append(4)
            check = False

        else:
            check = True
            a.append(4)
            N -= 4
            b.append(5)

    if M != 1:
        a.append(5)
        b.append(6)

    else:
        a.append(5)
        b.append(5)

    # print(*a, sep="")
    pass
    # print(*b, sep="")
    pass
if __name__ == "__main__":
    # 示例：可以修改这里的 n 来改变规模
    main(20)