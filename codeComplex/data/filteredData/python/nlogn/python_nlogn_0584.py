def main(n):
    if n <= 0:
        return
    if n == 1:
        print(1)
        return

    a = []
    for i in range(1, n + 1, 2):
        a.append(1)

    b = []
    for i in range(2, n + 1, 2):
        b.append(i)

    p = len(b)
    k = 2

    while p > 0:
        c = []
        for i in range(p):
            if b[i] % k == 0 and b[i] % (k * 2) != 0:
                a.append(k)
                p -= 1
            else:
                c.append(b[i])
        b = c[:]
        k = k * 2

    p = a[-1] // 2
    a.pop()
    q = p
    for i in range(p, n + 1):
        if i % p == 0 and i > q:
            q = i
    a.append(q)

    for i in a:
        print(i, end=" ")


if __name__ == "__main__":
    # 示例：以 n = 10 作为输入规模运行
    main(10)