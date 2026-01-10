def main(n):
    # 输入规模含义：
    # n = 原程序中的 n
    # 构造一个确定性的长度为 n 的数组 a
    # 这里使用简单的算术构造：a[i] = i // 2
    a = [i // 2 for i in range(n)]
    a.sort()

    if n == 1:
        if a[0] % 2 == 1:
            v = True
        else:
            v = False
    else:
        v = True
        c = 0
        j = -1
        for i in range(0, n - 1):
            if a[i] == a[i + 1]:
                c = c + 1
                j = i
        if c > 1:
            v = False
        elif c == 1:
            if a[j] == 0:
                v = False
            if j > 0:
                if a[j - 1] + 1 == a[j]:
                    v = False
        if (sum(a) - (n * (n - 1)) // 2) % 2 == 0:
            v = False

    if v:
        print("sjfnb")
    else:
        print("cslnb")


if __name__ == "__main__":
    main(10)