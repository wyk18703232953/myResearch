def main(n):
    m = n if n > 0 else 1

    # 生成一个确定性的长度为 m 的整数序列，作为原程序的输入
    # 这里使用简单的算术构造：x_i = (i * (i + 1)) // 2
    xs = [(i * (i + 1)) // 2 for i in range(m)]

    b = []
    k = []
    for i in range(m):
        x = xs[i]
        c = 0
        for j in range(len(b)):
            v = b[j]
            d = k[j]
            if (x ^ v) < x:
                x ^= v
                c ^= d

        if x != 0:
            print(0)
            c ^= 2 ** i
            b.append(x)
            k.append(c)
        else:
            a = []
            cc = c
            for j in range(m):
                if cc & 1 == 1:
                    a.append(j)
                cc >>= 1
            print(len(a), end='')
            for v in a:
                print(' ', v, sep='', end='')
            print()


if __name__ == "__main__":
    main(10)